import csv
import re
import basicFunc as bf
def changeMonthtoYear(start): #'연봉' 열에서 월급을 연봉으로 바꾸어줍니다. 매개변수는 csv.Reader 혹은 csv.DictReader로 저장한 변수입니다.
    rows = list(start)
    # 각 행의 연봉 데이터를 수정합니다.
    for row in rows:
        salary = row['연봉']
        # if '연봉' in salary:
        #     # '연봉' 문자열이 있을 경우 4개의 숫자를 추출합니다.
        #     numbers = re.findall(r'\d+', salary)
        #     cleaned_salary = ''.join(numbers[:4])  # 처음 4개의 jt숫자만 추출
        if '월급' in salary:
            # '월급' 문자열이 있을 경우 숫자에 12를 곱하여 값을 추출합니다.
            numbers = re.findall(r'\d+', salary)
            cleaned_salary = str(int(numbers[0]) * 12)  # 숫자에 12를 곱함
        else:
            # '연봉' 또는 '월급' 문자열이 없을 경우 그대로 유지합니다.
            cleaned_salary = salary
        # 수정된 연봉 값을 업데이트합니다.
        row['연봉'] = cleaned_salary
    #수정된 데이터를 반환합니다.
    # Extracting column names from the first row
    fieldnames = list(rows[0].keys())

    # Creating a list of edited rows with all columns
    edited_rows = [fieldnames] + [list(row.values()) for row in rows]
    return edited_rows

def locationConv(reader):#'근무지' 열에서 필요없는 문구를 삭제합니다.
    #시도 리스트
    spc_district = ["서울특별시", "인천광역시", "대전광역시", "대구광역시", "울산광역시", "부산광역시", "광주광역시", "세종특별자치시"]
    spc_short = ['서울', '인천', '대전', '대구', '울산', '부산', '광주', '세종']
    do_district = ["경기도", "강원도", "충청북도", "충청남도", "전라북도", "전라남도", "경상북도", "경상남도", "제주특별자치도"]
    #짧은것을 길게 만들기위한 딕셔너리
    spc_short_dict = dict(zip(spc_short, spc_district))

    #행 데이터 초기화
    rows = list(reader)

    #각 행의 근무지 데이터를 수정합니다.
    for row in rows:
        location = row['근무지']
        #짧은 표현을 긴 표현으로 변경
        if any(short in location for short in spc_short):
            rfmdLocation = location
            for short, district in spc_short_dict.items():
                rfmdLocation = rfmdLocation.replace(short, district)
        
        #'근무지' 삭제
        #if '근무지' in location:
            #rfmdLocation = location.replace('근무지', '')

        #시도 리스트에 해당되지 않는 모든 문자 삭제
        rfmdLocation = remove_non_list_strings(location, spc_district + do_district)

        #수정된 근무지 값을 업데이트 합니다.
        row['근무지'] = rfmdLocation

    #수정된 데이터 반환
    # Extracting column names from the first row
    fieldnames = list(rows[0].keys())

    # Creating a list of edited rows with all columns
    edited_rows = [fieldnames] + [list(row.values()) for row in rows]

    return edited_rows

# 데이터를 이중으로 포함하고있는 연봉데이터를 최소 최대값으로 분리하여 새로운 열에 저장합니다.
def addMaxMinRow(reader):
        rows = list(reader)
        #각 행의 연봉을 수정합니다.
        for row in rows:
            salary = row['연봉']
            numbers = re.sub(r'[^0-9]','',salary)
            
            if len(numbers) == 8:
                #숫자가 8개 이상인 경우 숫자 4개씩을 최솟값과 최댓값으로 분리하여 저장합니다.
                min_salaries = numbers[:4]
                max_salaries = numbers[4:8]
                #print(min_salaries, max_salaries)
            else:
                #숫자가 8개 미만인 경우에는 빈 리스트로 저장힙니다.
                    min_salaries = []
                    max_salaries = []
            row['최솟값'] = str(min_salaries)
            row['최댓값'] = str(max_salaries)
            #row['최댓값'] = ''.join(max_salaries)

        #수정된 데이터를 반환
        #fieldnames = reader.fieldnames + ['최솟값', '최댓값'] #새로운 열 추가
        fieldnames = list(rows[0].keys()) + ['최솟값', '최댓값'] #새로운 열 추가
        edited_rows = [fieldnames] + [list(row.values()) for row in rows]
        return edited_rows

#연봉행 에서 필요한 데이터를 추출해 새로운 행에 저장합니다.
def addNewSalaries(reader):
    rows = list(reader)
    for row in rows:
        salary = row['연봉']
        #월급을 연봉으로 바꾸어 저장합니다.
        if '월급' in row:
            rfmd = strMonthToYear(salary)
        #연봉데이터만 추출합니다
        elif '연봉' in row:
            rfmd = strYearEdit(salary)
        row['edited_연봉'] = rfmd
    fieldnames = list(rows[0].keys())
    edited_rows = [fieldnames] + [list(row.values()) for row in rows]
    return edited_rows

#문자열에서 월급을 연봉으로 바꿉니다.
def strMonthToYear(strData):
    if '~' in strData: 
        allowed = ['~']
        reformed = removeNonListedNonDigit(strData,allowed)
        start, end = reformed.split('~') # 월급이 x ~ y 형태를 띄면 그 중간값을 사용함
        month = (int(start) + int(end))/ 2
        year = month * 12
        reformedStr = str(year)
    else:
        reformed= removeNonListedNonDigit(strData)
        year = int(reformed) * 12
        reformedStr = str(year)
    return reformedStr

#문자열에서 연봉을 단일 데이터로 추출합니다.
def strYearEdit(strData):
    reformedStr= ''
    if '~' in strData:
        allowed = ['~']
        reformed = removeNonListedNonDigit(strData,allowed)
        start, end = reformed.split('~')    #연봉이 x~y 형태를 띄면 그 중간값을 사용함
        year = int((int(start) + int(end)) / 2)
        reformedStr = str(year)
    else:
        reformedStr = removeNonListedNonDigit(strData)
    return reformedStr
        
#문자열에서 리스트에 있지 않는 모든 문자를 제거 합니다.
def remove_non_list_strings(string, allowed_strings):
        filtered_string = ' '.join(word for word in string.split() if word in allowed_strings)
        return filtered_string

#문자열에서 숫자와 리스트에 지정되지 않는 모든 문자를 삭제합니다.
def removeNonListedNonDigit(data, listed=['']):
    """
    This function removes all non-digit characters from the given data except the ones listed in the 'listed' parameter.
    """
    # Convert the listed characters to a set for faster lookup
    listed_set = set(listed)
    # Initialize an empty string to store the result
    result = ""
    # Loop through each character in the data
    for char in data:
        # Check if the character is a digit or listed
        if char.isdigit() or char in listed_set:
            # If it is, add it to the result string
            result += char
    # Return the result string
    return result