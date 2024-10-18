import requests
import os
from dotenv import load_dotenv



# DART API Key (발급받은 API 키를 입력하세요)
load_dotenv()
api_key = os.getenv('OPEN_API_KEY')
rcept_no = '20240312000736'  # 원하는 공시 서류의 접수번호 (예시)

# 요청 URL
url = f'https://opendart.fss.or.kr/api/document.xml?crtfc_key={api_key}&rcept_no={rcept_no}'

# API 호출 (GET 요청으로 Zip 파일 받기)
response = requests.get(url)

# 응답 상태 코드 확인 (정상적인 응답은 200)
if response.status_code == 200:
    # 파일이 zip 형식으로 올 경우 저장
    with open(f'document_{rcept_no}.zip', 'wb') as file:
        file.write(response.content)
    print(f"공시서류 원본 파일이 'document_{rcept_no}.zip'으로 저장되었습니다.")
else:
    # 에러 메시지 출력
    print(f"파일 다운로드 실패: {response.status_code}")
    print(response.text)