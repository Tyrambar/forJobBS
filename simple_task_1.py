from bs4 import BeautifulSoup as Bs
import requests
import re
import string as st

from for_task_1 import *

from random import choice
from openpyxl import Workbook
from csv import writer

params_company[0] = "Характеристики компании"
while True:
    inp_url = input().lower()
    if re.match(r'\d+', inp_url):
        break

head_cells = ["{}{}".format('A', numb+1) for numb in range(len(params_company))]
wb = Workbook()
ws = wb.active
for numb, cell in enumerate(head_cells):
    ws[cell] = params_company[numb]
url = '{}{}'.format(main_url, inp_url)
for i in range(20):
    useragent = {'User-agent': choice(useragents)}
    try:
        req = requests.get(url, headers=useragent)
    except:
        pass
    else:
        break

bs = Bs(req.text, "html.parser")
ans = get_params(bs)
for n, param in enumerate(params_company[1:]):
    main_cells = ["{}{}".format('B', numb + 2) for numb in range(len(params_company[1:]))]
    for num, cell in enumerate(main_cells):
        ws[cell] = ans[params_company[num+1]]

path = "for_task_1_simple.csv"
with open(path, "w", newline='') as for_task_1_simple:
    write = writer(for_task_1_simple, delimiter=",")
    write.writerow([params_company[0],''])
    for line in range(len(params_company[:-1])):
        write.writerow([params_company[line+1], ans[params_company[line+1]]])

wb.save("for_task_1_simple.xlsx")


