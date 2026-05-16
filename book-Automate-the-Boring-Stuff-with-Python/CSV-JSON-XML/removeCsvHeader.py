import csv,os
os.makedirs('headerRemoved',exist_ok=True)
for csv_file in os.listdir('removeCsvHeader'):
    if not csv_file.endswith('.csv'):
        continue
    print('removing header from ' + csv_file+'...')

    csv_rows=[]
    csv_file_obj=open(os.path.join('removeCsvHeader',csv_file),'r',encoding='utf-8')
    reader_obj=csv.reader(csv_file_obj)
    for row in reader_obj:
        if reader_obj.line_num == 1:
            continue
        csv_rows.append(row)
    csv_file_obj.close()

    csv_file_obj=open(os.path.join('headerRemoved',csv_file),'w',newline='')
    csv_writer=csv.writer(csv_file_obj)
    for row in csv_rows:
        csv_writer.writerow(row)
    csv_file_obj.close()
