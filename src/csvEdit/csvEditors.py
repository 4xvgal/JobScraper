import csv
import re
import pandas as pd
from . import basicFunc as bf
#import basicFunc as bf

def locationConv(reader):#'근무지' 열에서 필요없는 문구를 삭제합니다.
    spc_district = ["서울특별시", "인천광역시", "대전광역시", "대구광역시", "울산광역시", "부산광역시", "광주광역시", "세종특별자치시"]
    spc_short = ['서울', '인천', '대전', '대구', '울산', '부산', '광주', '세종']
    do_district = ["경기도", "강원도", "충청북도", "충청남도", "전라북도", "전라남도", "경상북도", "경상남도", "제주특별자치도"]
    spc_short_dict = dict(zip(spc_short, spc_district))
    spc_short_dict.update({
    '경남': '경상남도','경기': '경기도', '경북': '경상북도','전남': '전라남도' ,'전북': '전라북도', '충남':'충청남도', '충북':'충청북도'
    })
    #짧은것을 길게 만들기위한 딕셔너리
    
    rows = list(reader)


    #각 행의 근무지 데이터를 수정합니다.
    for row in rows:
        location = row['근무지']
        #짧은 표현을 긴 표현으로 변경
        for short, full in spc_short_dict.items():
            location = re.sub(short, full, location)

        rfmdLocation = remove_non_list_strings(location, spc_district + do_district)
        row['근무지'] = rfmdLocation

    #수정된 데이터 반환
    # Extracting column names from the first row
    fieldnames = list(rows[0].keys())
    edited_rows = [fieldnames] + [list(row.values()) for row in rows]

    return edited_rows
  
#문자열에서 리스트에 있지 않는 모든 문자를 제거 합니다.
def remove_non_list_strings(string, list_):
    if any(substring in string for substring in list_):
        for item in list_:
            if item in string:
                return item
    else:
        return string
    

def modify_education_column(importPath, exportPath,):
    # CSV 파일을 pandas 데이터프레임으로 읽어오기
    data = pd.read_csv(importPath, encoding='cp949')

    # 학력 열 데이터 수정
    for i in range(len(data['학력'])):
        if '학력' not in data['학력'][i]:
            data['학력'][i] = data['학력'][i][:2]

    # 수정된 데이터 확인
    print(data['학력'])

    # 수정된 데이터를 CSV 파일로 저장
    data.to_csv(exportPath, index=False, encoding='cp949')
