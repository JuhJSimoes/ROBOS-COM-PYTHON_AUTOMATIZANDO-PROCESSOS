from bs4 import BeautifulSoup

html_file = open(
    "AUTOMACAO_PYTHON_SELENIUM-WEB_SCRAPING_BS4\\arquivos\\generic_simple.html", mode='r', encoding='utf-8')
soup = BeautifulSoup(html_file, features='html.parser')
print(soup.title.string, '\n')
print(soup.title.parent, '\n')
print(soup.title.parent.parent.name, '\n')
print(soup.div, '\n')
print(list(soup.div.children), '\n')
print(soup.p.string, '\n')


print(soup.find('div'), '\n')
print(soup.find('div', id='imp_article_ID'), '\n')
print(soup.find('div', class_='article'), '\n') #underline depois do class_ representa contem
print(soup.find_all('a'), '\n')
print(len(soup.find_all('a')), '\n')



# print(html_file)
# print(soup.prettify())
# print(soup.get_text())
