import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import font_manager, rc
import re

def draw_graph(ax, canvas, cleand, keyword = "default"):
    "cleand 가 경로"
     
    font_name = font_manager.FontProperties(fname=r"c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)

    # CSV 파일을 pandas 데이터프레임으로 읽어오기
    data = pd.read_csv(cleand, encoding='cp949')

    # '경력' 열에서 경력 값만 추출하여 리스트로 변환
    def convert_career(career):
        # 정규 표현식을 사용하여 숫자를 추출
        numbers = re.findall('\d+', career)

        if not numbers:  # 숫자 추출이 실패한 경우
            return 0

     # 숫자들 중 최솟값을 반환
        numbers = list(map(int, numbers))
        return min(numbers)

    data['경력'] = data['경력'].apply(convert_career)
    careers = data['경력'].tolist()


    # 경력 히스토그램 생성

    plt.xticks(fontsize=6.5)
    ax.hist(careers, bins=10, edgecolor='black')

    # 그래프 제목과 축 레이블 설정
    ax.set_title(keyword + '경력 히스토그램')
    ax.set_xlabel('연차')
    ax.set_ylabel('빈도')
    
    canvas.draw()
