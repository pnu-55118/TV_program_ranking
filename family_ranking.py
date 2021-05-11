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
a = [[], [], [], []]

i = 0
j = 1
# 7 8 9 10 // 3 0 1 2
for data in k[0]:
    if i < 6:
        i += 1
        continue
    if j % 4 == 3:
        a[0].append(data)

    if j % 4 == 0:
        a[1].append(data)
    if j % 4 == 1:
        a[2].append(data)
    if j % 4 == 2:
        a[3].append(data)
    j += 1
    i += 1


# 순위 채널 프로그램 시청자수
# a = [[순위],[채널],[프로그램],[시청률]]
# a[2] , a[3]
# b = [[순위],[채널],[프로그램],[시청자수]]
# b[2], b[3]

print(a)
print(a[1])
import matplotlib.pyplot as plt
for k in range(len(a[1])):
    a[1][k]=float(a[1][k])
plt.rc('font', family='Malgun Gothic')

x=list(range(1,21))
program=a[0]
plt.plot(x,a[1])
plt.xticks(x,program,rotation='vertical')
plt.show()
