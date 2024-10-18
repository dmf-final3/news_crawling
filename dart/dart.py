import requests
import os
from dotenv import load_dotenv



# DART API Key (발급받은 API 키를 입력하세요)
load_dotenv()
api_key = os.getenv('OPEN_API_KEY')

# 특정 기업의 종목 코드 (예: LG생활건강)
corp_code = '051900'

# 특정 기업의 공시 목록을 불러오는 URL
url = f'https://opendart.fss.or.kr/api/list.json?crtfc_key={api_key}&corp_code={corp_code}&bgn_de=20240318&end_de=20240318&last_reprt_at=Y'

# API 호출 (GET 요청)
response = requests.get(url)
data = response.json()

# 공시 목록에서 첫 번째 공시의 rcept_no 추출
if 'list' in data and len(data['list']) > 0:
    rcept_no = data['list'][0]['rcept_no']
    print(f'공시번호 (rcept_no): {rcept_no}')
else:
    print("공시 목록을 찾을 수 없습니다.")

    # DART API Key (발급받은 API 키를 입력하세요)
api_key = 'YOUR_API_KEY'

# 공시번호 (위에서 조회한 공시번호)
rcept_no = '20240318000000'  # 예시로 사용 (위 코드에서 얻은 rcept_no를 사용해야 함)

# 공시서류 원본 파일을 불러오는 URL
file_url = f'https://opendart.fss.or.kr/api/document.xml?crtfc_key={api_key}&rcept_no={rcept_no}'

# API 호출 (GET 요청)
response = requests.get(file_url)

# 응답을 파일로 저장
file_name = f'{rcept_no}_original_document.xml'
with open(file_name, 'wb') as file:
    file.write(response.content)

print(f'공시서류 원본 파일이 {file_name}로 저장되었습니다.')