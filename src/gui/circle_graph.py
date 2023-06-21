import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import font_manager, rc
import os

def draw_graph(ax, canvas, cleand):

    
  
    font_name = font_manager.FontProperties(fname=r"c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)

    data = pd.read_csv(cleand, encoding='cp949')

    # 지역별 일자리 갯수 계산
    job_counts = data['근무지'].value_counts()

    # 상위 2개 지역 이름 유지, 나머지는 '기타'로 묶음
    top_two_regions = job_counts.nlargest(2)
    other_regions = job_counts.iloc[2:].sum()
    top_two_regions['기타'] = other_regions

    # 원 그래프 생성
    ax.pie(top_two_regions, labels=top_two_regions.index, autopct='%1.1f%%', startangle=90)

    # 그래프 스타일 설정
    ax.set_title('Job counts by region (minor regions grouped as "others")')
    ax.plot
    canvas.draw()
    
    
