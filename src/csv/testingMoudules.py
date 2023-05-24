#모듈 테스트를 위한 예제
import csv
import re
import csvEditors as ce
import basicFunc as bf

file_path = "src/csv/forTestFiles/data2.csv"
export_path = "src/csv/forTestFiles/cleaned.csv"


# #월봉을 연봉으로 바꾸기
# with open(file_path, 'r',encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     cleaned_data = ce.changeMonthtoYear(reader)
#     bf.save_to_csv(cleaned_data,export_path,'utf-8',False)

#근무지 데이터 간소화 (연봉 이중데이터 전환보다 먼저 실행되어야함)
with open(file_path,'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    cleaned_data = ce.locationConv(reader)
    bf.save_to_csv(cleaned_data,export_path,'utf-8',False)

#연봉행 데이터 가공하기
with open(export_path,'r',encoding='utf-8') as file:
    reader = csv.DictReader(file)
    cleaned_data = ce.addNewSalaries(reader)
    bf.save_to_csv(cleaned_data,export_path,'utf-8',True)

