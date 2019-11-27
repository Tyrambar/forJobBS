from bs4 import BeautifulSoup as Bs
import requests
import re
import string as st

from for_task_1 import *

from random import choice
from openpyxl import Workbook
from csv import writer

params_company[0] = "№"
companies = []
while True:
    inp_url = input().lower()
    if re.match(r'({})\d+'.format(main_url), inp_url):
        appended_url = re.sub('{}'.format(main_url), '', inp_url)
        companies.append(re.sub(' ', '', appended_url))
    if inp_url.lower() == 'stop':
        break

head_cells = ["{}{}".format(st.ascii_uppercase[numb], 1) for numb in range(len(params_company))]
wb = Workbook()
ws = wb.active

for numb, cell in enumerate(head_cells):
    ws[cell] = params_company[numb]

path = "for_task_1_complic.csv"
with open(path, "w", newline='') as for_task_1_complic:
    write = writer(for_task_1_complic, delimiter=",")
    write.writerow(params_company)
    for numb, company in enumerate(companies):
        for i in range(20):
            useragent = {'User-agent': choice(useragents)}
            try:
                req = requests.get('{}{}'.format(main_url, company), headers=useragent)
            except:
                pass
            else:
                break
        bs = Bs(req.text, "html.parser")
        ans = get_params(bs)
        main_cells = ["{}{}".format(st.ascii_uppercase[num+1], numb+2) for num in range(len(params_company[1:]))]
        ws["A"+str(numb+2)] = numb+1
        row_csv = [numb+1]
        for num, cell in enumerate(main_cells):
            ws[cell] = ans[params_company[num + 1]]
            row_csv.append(ans[params_company[num + 1]])
        write.writerow(row_csv)

wb.save("for_task_1_complic.xlsx")