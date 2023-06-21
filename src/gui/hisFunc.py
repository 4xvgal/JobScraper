import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import font_manager, rc


def draw_graph(ax, canvas, cleand, keyword = "default"):
    font_name = font_manager.FontProperties(fname=r"c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
# CSV 파일 읽어들이기
    data = pd.read_csv(cleand,encoding='cp949')

# 근무지별 학력 데이터 집계
    education_counts = data.groupby('근무지')['학력'].value_counts().unstack().fillna(0)

# 학력 막대 그래프 생성
    education_counts.plot(kind='bar', stacked=True)

# 그래프 제목과 축 레이블 설정
    ax.set_title('지역별 학력 분포')
    ax.set_xlabel('근무지')
    ax.set_ylabel('인원 수')

# 그래프 표시
    canvas.draw()

