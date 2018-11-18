from selenium import webdriver
from bs4 import BeautifulSoup

driver= webdriver.Chrome()

driver.get('https://www.instagram.com/michaeljackson/')
soup = BeautifulSoup(driver.page_source,"lxml")
driver.quit()

for item in soup.select('._o6mpc'):
    name = item.select('._kc4z2')[0].text
    followers= item.select('._fd86t')[1].text
    following = item.select('._fd86t')[2].text
    print('Name :{}\nFollowers :{}\nFollowing :{}'.format(name,followers,following)