#모듈 테스트를 위한 예제
import csv
import re
import csvEditors as ce
import basicFunc as bf

file_path = "src/csv/forTestFiles/data2.csv"
export_path = "src/csv/forTestFiles/cleaned.csv"

#월봉을 연봉으로 바꾸기
with open(file_path, 'r',encoding='utf-8') as file:
    reader = csv.DictReader(file)
    cleaned_data = ce.changeMonthtoYear(reader)
    bf.save_to_csv(cleaned_data,export_path,'utf-8',True)

# # #이중데이터 (2000만 ~ 4000만) 데이터 분리 ()
# with open(export_path,'r',encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     cleaned_data = ce.addMaxMinRow(reader)
#     bf.save_to_csv(cleaned_data,export_path,'utf-8',True)

# #근무지 데이터 간소화
with open(export_path,'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    cleaned_data = ce.locationConv(reader)
    bf.save_to_csv(cleaned_data,export_path,'utf-8',True)
