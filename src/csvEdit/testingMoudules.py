#모듈 테스트를 위한 예제
import csv
import re
import csvEditors as ce
import basicFunc as bf

import csvFunc as cf
file_path = "src/csv/merged.csv"
export_path = "src/csv/merged_cleaned.csv"
cf.csvEdit(file_path, export_path,'cp949')
