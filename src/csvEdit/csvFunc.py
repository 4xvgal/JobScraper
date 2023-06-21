#csv 재가공 프로그램
#근무지를 간소화합니다.
#최솟값과 최대값을 가지는 연봉, 월급데이터를 중간값으로 바꿉니다. 연봉행에서 월급을 연봉으로 바꿉니다. 
import csv
#import csvEditors as ce
from . import csvEditors as ce
from . import basicFunc as bf
#import basicFunc as bf
def csvEdit(importPath, exportPath, env_encoder): #csvEdit은 입력경로와 출력경로, 인코딩방식을 인자로 받습니다. 리턴은 없습니다.
    with open(importPath, 'r', encoding = env_encoder) as file:
        reader = csv.DictReader(file)
        cleaned_data = ce.locationConv(reader) #근무지 행 수정
        bf.save_to_csv(cleaned_data,exportPath,env_encoder,False)
    with open(exportPath, 'r', encoding=env_encoder) as file:
        reader = csv.DictReader(file)
        cleaned_data = ce.addNewSalaries(reader) #연봉행 수정
        bf.save_to_csv(cleaned_data,exportPath,env_encoder,False)
