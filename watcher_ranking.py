from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.nielsenkorea.co.kr/tv_terrestrial_day.asp?menu=Tit_1&sub_menu=1_1&area=01&begin_date=20210509'
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
ranks = soup.find_all('table', {'class': 'ranking_tb'})

k = []
for rank in ranks:
    k.append(rank.text.split('\n'))

for j in range(0, 2):
    i = 0
    while i < len(k[j]):
        k[j][i] = k[j][i].strip()
        if k[j][i] == '' or k[j][i] == ' ':
            del k[j][i]
            i -= 1
        k[j][i] = k[j][i].replace('\t', '')
        k[j][i] = k[j][i].replace('\r', '')
        k[j][i] = k[j][i].replace(' ', '')
        i += 1

# k[0] = 가구시청률 k[1] = 시청자수
# 6~

b = [[], [], [], []]


i = 0
j = 1
for data in k[1]:
    if i < 6:
        i += 1
        continue
    if j % 4 == 3:
        b[0].append(data)
    if j % 4 == 0:
        b[1].append(data)
    if j % 4 == 1:
        b[2].append(data)
    if j % 4 == 2:
        b[3].append(data)
    j += 1
    i += 1

# 순위 채널 프로그램 시청자수
# a = [[순위],[채널],[프로그램],[시청률]]
# a[2] , a[3]
# b = [[순위],[채널],[프로그램],[시청자수]]
# b[2], b[3]

# for k in range(len(b[1])):
#     b[1].replace(b[1][k],float(b[1][k]))
# print(b[1])

# for i in b[1]:
#     if ',' in i:
#         i=i.remove(',')
# for k in range(len(b[1])):
#     b[1].replace(b[1][k],float(b[1][k]))

# for i in b[1]:
#     if ',' in i:
#         t=i.split(',')
#         i=t[0]+t[1]
#         print(i)



# for k in range(len(b[1])):
    # b[1][k]=float(b[1][k])

for i in range(len(b[1])):
    if ','in b[1][i]:
        b[1][i]=b[1][i].replace(',','')


import matplotlib.pyplot as plt
for k in range(len(b[1])):
    b[1][k]=float(b[1][k])
plt.rc('font', family='Malgun Gothic')

x=list(range(1,21))
program=b[0]
plt.plot(x,b[1])
plt.xticks(x,program,rotation='vertical')
plt.show()
