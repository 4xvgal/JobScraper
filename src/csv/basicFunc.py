import csv
import os
#File 데이터를 함수로 받아 csv_file_path에 csv파일로 저장합니다. indi 는 작동유무를 출력합니다. true or false
def save_to_csv(data, csv_file_path, encode = 'cp949' ,indi = False):
    with open(csv_file_path, mode='w', newline='',encoding= encode) as file:
        writer = csv.writer(file)
        writer.writerows(data)
        # indi 인자가 true 이면 정상적으로 실행완료 하였다고 출력한다.
        if indi == True:
            print('Saving successfuly done')
#def save_dictWirter(data,fieldnames, csv_file_path, encode ='cp949', indi = False):
    #with open(csv_file_path,'w', newline='',encoding=encode) as file:
                #writer = csv.DictWriter(file, fieldnames=fieldnames)
                #writer.writeheader()
                #writer.writerows(rows)