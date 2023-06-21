#모듈 테스트를 위한 예제
import csv
import re
from . import csvFunc
#import csvFunc as cf
file_path = r"C:\CSV\merged.csv"
export_path = r"C:\CSV\merged.cleaned.csv"
csvEdit(file_path, export_path,'cp949')
