#근무지 데이터 간소화 (연봉 이중데이터 전환보다 먼저 실행되어야함)
with open(export_path,'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    cleaned_data = ce.locationConv(reader)
    bf.save_to_csv(cleaned_data,export_path,'utf-8',False)