import dart_fss as dart
import os
from dotenv import load_dotenv
import pandas as pd



# DART API Key (발급받은 API 키를 입력하세요)
load_dotenv()

# Open DART API KEY 설정
api_key = os.getenv('OPEN_API_KEY')
dart.set_api_key(api_key=api_key)

# DART 에 공시된 회사 리스트 불러오기
corp_list = dart.get_corp_list()

# 삼성전자 검색
samsung = corp_list.find_by_corp_name('삼성전자', exactly=True)[0]

# # 2019년 3월 1일부터 2019년 5월 31일까지 삼성전자의 모든 공시 정보 조회
# reports = samsung.search_filings(bgn_de='20190301', end_de='20190531')
# reports

# # 2010년 1월 1일부터 현재까지 모든 사업보고서 검색
# reports = samsung.search_filings(bgn_de='20100101', pblntf_detail_ty='a001')
# reports

# 2010년 1월 1일부터 현재까지 모든 사업보고서의 최종보고서만 검색
reports = samsung.search_filings(bgn_de='20100101', pblntf_detail_ty='a001', last_reprt_at='Y')
reports

# # 2010년 1월 1일부터 현재까지 사업보고서, 반기보고서, 분기보고서 검색
# reports = samsung.search_filings(bgn_de='20100101', pblntf_detail_ty=['a001', 'a002', 'a003'])
# reports

# 가장 최신 보고서 선택
newest_report = reports[0]

# 첨부파일 목록
attached_files = newest_report.extract_attached_files()

# 첨부보고서 목록
attached_reports = newest_report.extract_attached_reports()

# 첨부파일 목록을 pandas DataFrame으로 변환
df_files = pd.DataFrame(attached_files)

# 첨부보고서 목록을 pandas DataFrame으로 변환
df_reports = pd.DataFrame(attached_reports)

# 엑셀 파일로 저장
with pd.ExcelWriter('report_files_and_reports.xlsx') as writer:
    df_files.to_excel(writer, sheet_name='Attached Files', index=False)
    df_reports.to_excel(writer, sheet_name='Attached Reports', index=False)