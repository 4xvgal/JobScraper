import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

def create_histogram(file_path):
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)

    # CSV 파일을 pandas DataFrame으로 읽어옵니다.
    data = pd.read_csv(file_path, encoding='cp949')

    # 히스토그램을 생성할 열의 데이터를 선택합니다.
    edited_salaries = data['edited_연봉']

    # 히스토그램 생성을 위한 설정
    plt.figure(figsize=(10, 6))  # 그래프 크기 설정
    plt.hist(edited_salaries, bins=10)  # 히스토그램 생성 (구간 수는 bins 매개변수로 조정 가능)

    # 그래프에 제목과 축 레이블 추가
    plt.title('연봉 분포')
    plt.xlabel('연봉')
    plt.ylabel('빈도')

    # 그래프 출력
    plt.show()

# 함수 호출 예시
file_path = 'C:\CSV\cleaned.csv'
create_histogram(file_path)

