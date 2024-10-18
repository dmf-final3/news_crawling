from bs4 import BeautifulSoup
import requests
import csv

# XML 파일을 가져올 URL 설정
url = 'https://news.google.com/rss/search?q=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90%20after%3A2020-10-15%20before%3A2024-10-14&hl=ko&gl=KR&ceid=KR%3Ako'

# URL에서 XML 파일 가져오기
response = requests.get(url)
xml_data = response.content

# BeautifulSoup을 사용해 XML 데이터를 파싱
soup = BeautifulSoup(xml_data, 'xml')

# CSV 파일을 쓰기 모드로 열기
with open('news_data.csv', mode ='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    #CSV 파일에 헤더(컬럼 이름) 추가
    writer.writerow(['title', 'link', 'pubDate'])

    #XML에서 <item> 태그들 찾기 (뉴스 기사가 있는 부분)
    items = soup.find_all('item')

    #각 <item>에서 제목, 링크, 발행일을 추출해서 CSV 파일에 저장
    for item in items:
        title = item.find('title').get_text()
        link = item.find('link').get_text()
        pub_date = item.find('pubDate').get_text()

        #각 기사의 정보를 한 줄씩 CSV 파일에 쓰기
        writer.writerow([title, link, pub_date])

print("CSV 파일로 저장되었습니다.")