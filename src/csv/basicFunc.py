import csv
import os
#File 데이터를 함수로 받아 csv_file_path에 csv파일로 저장합니다.
def save_to_csv(data, csv_file_path):
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
        print('Saving successfuly done')