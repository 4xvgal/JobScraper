import csv

def saveToCsv(data, destination): #data 변수에 저장된 csv 데이터를 destination 경로에 새 파일로 저장합니다.
    # 수정된 데이터를 CSV 파일로 저장합니다.
    rows= list(data)
    output_file_path = destination # 저장할 파일 경로 수정
    fieldnames = data.fieldnames
    with open(output_file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

