#모듈 테스트를 위한 예제
import csv
import re
import salaries as sl
import basicFunc as bf

file_path = "src/csv/forTestFiles/data1.csv"
export_path = "src/csv/forTestFiles/cleaned.csv"

with open(file_path, 'r', encoding='cp949') as file:
    reader = csv.DictReader(file)
    
    cleaned_data = sl.changeMonthtoYear(reader)
    bf.save_to_csv(cleaned_data,export_path)

with open(file_path,'r', encoding='cp949') as file:
    reader = csv.DictReader(file)
    cleaned_data = sl.locationConv(reader)
    bf.save_to_csv(cleaned_data,export_path)