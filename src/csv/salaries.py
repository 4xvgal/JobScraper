import csv
import re

def changeMonthtoYear(start): #'연봉' 열에서 월급을 연봉으로 바꾸어줍니다.
    salaries = start['연봉']
    rows = list(start)

    # 각 행의 연봉 데이터를 수정합니다.
    for row in rows:
        salary = row['연봉']

        if '연봉' in salary:
            # '연봉' 문자열이 있을 경우 4개의 숫자를 추출합니다.
            numbers = re.findall(r'\d+', salary)
            cleaned_salary = ''.join(numbers[:4])  # 처음 4개의 숫자만 추출
        elif '월급' in salary:
            # '월급' 문자열이 있을 경우 숫자에 12를 곱하여 값을 추출합니다.
            numbers = re.findall(r'\d+', salary)
            cleaned_salary = str(int(numbers[0]) * 12)  # 숫자에 12를 곱함
        else:
            # '연봉' 또는 '월급' 문자열이 없을 경우 그대로 유지합니다.
            cleaned_salary = salary

        # 수정된 연봉 값을 업데이트합니다.
        row['연봉'] = cleaned_salary
    return cleaned_salary
