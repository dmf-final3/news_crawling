# 필요한 라이브러리 가져오기
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import csv
import time  # 요청 사이에 잠시 쉬기 위해 사용

# XML 파일을 가져올 URL 설정
url = 'https://news.google.com/rss/search?q=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90%20after%3A2020-10-15%20before%3A2024-10-14&hl=ko&gl=KR&ceid=KR%3Ako'

# URL에서 XML 파일 가져오기
response = requests.get(url)
xml_data = response.content

# BeautifulSoup을 사용해 XML 데이터를 파싱
soup = BeautifulSoup(xml_data, 'xml')

# CSV 파일을 쓰기 모드로 열기
with open('news_with_content.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # CSV 파일에 헤더(컬럼 이름) 추가
    writer.writerow(['Title', 'Link', 'PubDate', 'Content'])

    # XML에서 <item> 태그들 찾기 (뉴스 기사가 있는 부분)
    items = soup.find_all('item')

    # 각 <item>에서 제목, 링크, 발행일을 추출하고 기사 본문 크롤링
    for item in items:
        title = item.find('title').get_text()
        link = item.find('link').get_text()
        pub_date = item.find('pubDate').get_text()

        # 기사 본문 크롤링을 시도
        try:
            article_response = requests.get(link)
            article_soup = BeautifulSoup(article_response.content, 'html.parser')

            # 기사 본문에서 <div> 태그의 텍스트를 모두 모아서 content에 저장 (예시: <div> 태그로 본문을 구성한 경우)
            paragraphs = article_soup.find_all('div')
            content = ' '.join([para.get_text() for para in paragraphs])

            # 기사 본문이 너무 짧으면 실패로 간주
            if len(content) < 50:  # 본문 길이가 너무 짧을 경우 크롤링 실패로 간주
                content = "Content not available or too short."

        except Exception as e:
            content = "Failed to retrieve content."

        # 각 기사의 정보를 한 줄씩 CSV 파일에 쓰기
        writer.writerow([title, link, pub_date, content])

        # 요청 사이에 잠시 쉬기 (웹사이트에 부담을 줄 수 있으므로)
        time.sleep(2)

print("CSV 파일로 저장되었습니다.")