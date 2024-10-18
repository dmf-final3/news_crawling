import json
import requests
import pandas as pd

# 요청 URL
url = "https://www.bigkinds.or.kr/api/news/search.do"

# 요청 헤더 설정
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate", 
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,und;q=0.6",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://www.bigkinds.or.kr",
    "Referer": "https://www.bigkinds.or.kr/v2/news/search.do",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
}

# 페이로드 데이터 (검색어 및 기간 설정)
payload = {
    "indexName": "news",
    "searchKey": "LG에너지솔루션",  # 키워드 설정
    "searchKeys": [{}],
    "byLine": "",
    "searchFilterType": "1",         # 기본 검색 필터 (뉴스 본문 내에서 검색)
    "searchScopeType": "1",          # 검색 범위 (전체)
    "searchSortType": "date",        # 날짜 순으로 정렬
    "sortMethod": "date",            # 날짜별 정렬
    "mainTodayPersonYn": "",         # 오늘의 주요 인물 관련 필터 (제거)
    "startDate": "2023-01-01",       # 검색 시작 날짜
    "endDate": "2024-12-31",         # 검색 종료 날짜
    "newsIds": [],                   # 뉴스 ID 필터 (비우기)
    "categoryCodes": [],             # 카테고리 코드 필터 (비우기)
    "providerCodes": [],             # 언론사 필터 (비우기)
    "incidentCodes": [],             # 사건 코드 필터 (비우기)
    "networkNodeType": "",
    "topicOrigin": "",
    "dateCodes": [],
    "editorialIs": False,            # 편집된 기사 여부 (제거)
    "startNo": 1,                    # 시작 번호
    "resultNumber": 10,              # 한 번에 불러올 기사 수
    "isTmUsable": False,
    "isNotTmUsable": False
}

# 세션 생성 및 POST 요청
session = requests.Session()
session.headers.update(headers)
response = session.post(url, json=payload)

# # 응답 처리
# if response.status_code == 200:
#     data = response.json()
    
#     # JSON 데이터에서 필요한 부분만 추출 (기사 제목, 언론사, 링크, 작성일, 내용 등)
#     articles = data.get("resultList", [])
    
#     # 필요한 데이터 추출 후 리스트에 저장
#     extracted_data = []
#     for article in articles:
#         extracted_data.append({
#             "press": article.get("providerName"),  # 언론사
#             "title": article.get("title"),         # 기사 제목
#             "nlink": article.get("newsId"),        # 기사 링크 (ID 기반)
#             "date": article.get("regDate"),        # 기사 작성일
#             "body": article.get("content")         # 기사 내용
#         })
    
#     # DataFrame으로 변환
#     df = pd.DataFrame(extracted_data)

#     # CSV 파일로 저장
#     df.to_csv('news_data.csv', index=False, encoding='utf-8-sig')

#     print("CSV 파일이 성공적으로 생성되었습니다.")
# else:
#     print("뉴스 데이터를 가져오는 데 실패했습니다.", response.status_code)

# 응답 상태 코드 확인
print(f"응답 상태 코드: {response.status_code}")
print(f"응답 데이터: {response.text}")  # 전체 응답 내용 출력

# 만약 200 이외의 상태 코드가 나온다면 문제를 알 수 있을 것