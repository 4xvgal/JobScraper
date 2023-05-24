import tkinter as tk
import csv
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def search():
    query = entry.get()  # 검색 입력창의 텍스트 가져오기

    # CSV 파일 읽기
    with open('data.csv', 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # 헤더 라인 스킵

        # 검색 결과 필터링
        filtered_results = []
        for row in csv_reader:
            if query.lower() in [item.lower() for item in row]:  # 대소문자 구분 없이 검색
                filtered_results.append(row)

        # 검색 결과 표시
        result_label.config(text="검색 결과: " + query)
        result_text.delete('1.0', tk.END)  # 기존 텍스트 삭제
        for result in filtered_results:
            result_text.insert(tk.END, ', '.join(result) + '\n')

def show_graph():
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot([1, 2, 3, 4, 5], [2, 4, 1, 5, 2])

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

window = tk.Tk()
window.geometry("1280x720")  # 윈도우 해상도 설정

entry = tk.Entry(window)
entry.pack()

search_button = tk.Button(window, text="검색", command=search)
search_button.pack()

result_label = tk.Label(window, text="검색 결과:")
result_label.pack()

result_text = tk.Text(window, height=10, width=50)
result_text.pack()

graph_button = tk.Button(window, text="그래프 보기", command=show_graph)
graph_button.pack()

window.mainloop()
