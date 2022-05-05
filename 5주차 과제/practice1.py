import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'https://music.bugs.co.kr/chart'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

file = open('./pratice1.txt', 'w')
file.write(datetime.today().strftime('%Y년 %m월 %d일의 실시간 순위입니다.')+'\n')

results = soup.findAll('p', 'title')
for rank, result in enumerate(results):
    file.write(str(rank+1)+'위:'+result.get_text()+'\n')
