import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import font_manager, rc

def draw_graph(ax, canvas, cleand):
    "cleand 가 경로"
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    ax.plot(x, y)  # sin 함수를 그립니다.
    font_name = font_manager.FontProperties(fname=r"c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)

# CSV 파일 경로 지정
    csv_file_path = r"C:\CSV\merged.cleaned.csv"

# 데이터 로드
    data = pd.read_csv(csv_file_path, encoding='cp949')

# 지역별 일자리 갯수 계산
    job_counts = data['근무지'].value_counts().nlargest(10)

# 원 그래프 생성
    fig, ax = plt.subplots()
    ax.pie(job_counts, labels=job_counts.index, autopct='%1.1f%%', startangle=90)

# 그래프 스타일 설정
    ax.set_title('상위 6개 지역의 일자리 분포')
    canvas.draw()
    
