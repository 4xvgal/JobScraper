#모듈 테스트를 위한 예제
import csv
import re
import csvEditors as ce
import basicFunc as bf

import csvFunc as cf
file_path = "C:\CSV\merged.csv"
export_path = "C:\CSV\merged.cleaned.csv"
cf.csvEdit(file_path, export_path,'cp949')
