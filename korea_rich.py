from selenium import webdriver
import matplotlib
driver = webdriver.Chrome('C:\\Users\\user\\PycharmProjects\\untitled2\\chromedriver.exe')
url = 'https://www.forbes.com/?sh=390c4c1d2254'
driver.get(url)
data = []
data2 = [[],[]]
driver.find_element_by_xpath('/html/body/div[1]/header/nav/div[1]/button[1]').click()
driver.find_element_by_xpath('/html/body/div[1]/header/nav/div[3]/ul/li[1]').click()
driver.find_element_by_xpath('/html/body/div[1]/header/nav/div[3]/ul/li[1]/div[2]/ul/li[8]/a').click()
process1 = driver.find_element_by_xpath('//*[@id="list-table-body"]')
process2 = process1.find_elements_by_tag_name('td')
for i in process2:
    data.append(i.text)

i = 0
while (2+6*i)< (len(data)-1):
    data2[0].append(data[2+6*i])
    i += 1

i = 0
while (3+6*i)<(len(data)-1):
    data2[1].append(data[3+6*i])
    i+=1


for i in range(10):
    data2[1][i]=float(data2[1][i].replace('$','').replace('B',''))*1000000000
print(data2)
driver.quit()
# x = data2[0] y = data2[1]
