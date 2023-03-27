import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.gabrielcasemiro.com.br/')

if page.status_code == 200:
    #print(page.text.encode('utf-8'))
    soup = BeautifulSoup(page.text, 'html.parser')
    for link in soup.find_all('a'):
      print(link.get('href', ''))   
else:
    print('HTTP erro', page.status_code)
    
#soup = BeautifulSoup(page.text, 'html.parser')
#print(soup)
