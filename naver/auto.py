import requests
import json
from bs4 import BeautifulSoup as bts
import pandas as pd
import numpy as np
import time
from tqdm.notebook import tqdm
import os
import re
import datetime

def NaverNewsLink(searchWord, startNo=1, startDate='', endDate=''):
    res = requests.get(
        url='https://s.search.naver.com/p/newssearch/search.naver',
        params={
            'nqx_theme': {'theme': {'main': {'name': 'sports_event'}, 'sub': [{'name': 'issue'}]}},
            'query': searchWord,
            'sort': 0,
            'spq': 3,
            'pd': 0,
            'start': startNo,
            'where': 'news_tab_api',
            'ds': startDate,
            'de': endDate
        }
    )

    dic = json.loads(res.text)
    items = [bts(markup=i.strip(), features='html.parser') for i in dic['contents']]
    links = [item.select('a.info:last-child') for item in items]
    dates = [item.select('span.info')[0].text for item in items if len(item.select('span.info')) > 0]

    newsList = pd.DataFrame(data={
        'press': [item.select('a.press')[0].text for item in items],
        'title': [item.select('a.news_tit')[0].text for item in items],
        'nlink': [link[0]['href'] if len(link) >= 1 else np.nan for link in links],
        'date': dates
    })

    return newsList

def collect_year_news(searchWord, topN):
    newsList = pd.DataFrame()
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=365)
    
    for single_date in tqdm(pd.date_range(start_date, end_date)):
        start_date_str = single_date.strftime('%Y.%m.%d')
        df = NaverNewsLink(searchWord, startNo=1, startDate=start_date_str, endDate=start_date_str)
        newsList = pd.concat([newsList, df], ignore_index=True)
        time.sleep(1)

    # nlink가 결측인 행 삭제
    newsList = newsList.loc[newsList['nlink'].notna(), :]
    # press에서 '언론사 선정' 삭제
    newsList['press'] = newsList['press'].str.replace(pat='언론사 선정', repl='')
    # nlink에서 쿼리 문자열 삭제
    newsList['nlink'] = newsList['nlink'].str.replace(pat=r'(\?.+)', repl='', regex=True)
    # 중복된 nlink 확인 후 삭제
    newsList = newsList.drop_duplicates(subset='nlink').reset_index(drop=True)
    # 데이터프레임 저장
    pd.to_pickle(obj=newsList, filepath_or_buffer=f'Naver_News_List_{topN}.pkl')

def main():
    # 코스피 TOP 10 기업 리스트
    kospi_top10 = [
        '삼성전자', 'SK하이닉스', 'LG화학', '삼성바이오로직스', '현대차', 
        '셀트리온', 'NAVER', '카카오', '현대모비스', 'LG생활건강'
    ]

    for idx, company in enumerate(kospi_top10, start=1):
        collect_year_news(searchWord=company, topN=idx)
        print(f"{company} 뉴스 수집 완료 및 저장")

if __name__ == "__main__":
    main()