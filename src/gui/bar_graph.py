import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import font_manager, rc

def draw_graph(ax, canvas, cleand,keyword = "default"):
    "cleand 가 경로"
     
    font_name = font_manager.FontProperties(fname=r"c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)

    # CSV 파일을 pandas 데이터프레임으로 읽어오기
    data = pd.read_csv(cleand, encoding='cp949')

    # 경력 열에서 경력 값만 추출하여 리스트로 변환
    careers = data['경력'].tolist()

    # 여기서 '경력' 데이터를 수치형으로 변환하는 작업이 필요할 것 같습니다.
    # 이 부분은 데이터의 형식에 따라 적절히 처리해야 합니다.

    # 경력 히스토그램 생성
    ax.hist(careers, bins=10, edgecolor='black')

    # 그래프 제목과 축 레이블 설정
    ax.set_title(keyword + '경력 히스토그램')
    ax.set_xlabel('경력')
    ax.set_ylabel('빈도')
    
    canvas.draw()
