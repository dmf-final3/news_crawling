import dart_fss as dart
import os
from dotenv import load_dotenv
import pandas as pd



# DART API Key (발급받은 API 키를 입력하세요)
load_dotenv()
# Open DART API KEY 설정
api_key = os.getenv('OPEN_API_KEY')
dart.set_api_key(api_key)

# DART 공시 대상 회사들의 고유번호, 회사명, 대표자명, 종목 코드, 최근 변경 일자 정보를 다운로드
corp_info = dart.api.filings.get_corp_code()

# corp_info가 리스트 형태로 반환됨. 각 회사 정보는 리스트의 항목으로 접근
for info in corp_info:
    if info.get('stock_code').strip():
        print('=====info====')
        print(info)
        # corp_code = info.get('corp_code', 'N/A')  # 고유번호
        # corp_name = info.get('corp_name', 'N/A')  # 회사명
        # stock_code = info.get('stock_code', 'N/A')  # 종목 코드
        # ceo = info.get('ceo_nm', 'N/A')  # 대표자명
        # change_date = info.get('modify_date', 'N/A')  # 최근 변경 일자
    
    # print(f"회사명: {corp_name}, 종목 코드: {stock_code}, 고유번호: {corp_code}, 대표자명: {ceo}, 변경 일자: {change_date}")