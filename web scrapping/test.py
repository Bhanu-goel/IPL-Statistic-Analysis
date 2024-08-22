import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.teamoclock.com/free-tools/simple-timer')

print(r.url)

print(r.status_code)

soup = BeautifulSoup(r.content,'html.parser')

#print(soup.prettify())

print(soup.title)

# print(soup.title.name)

# print(soup.title.parent.name)

s=soup.find('div',class_='o-text-customEnormous u-fontSize-enormous@<SM u-color-light u-fontWeight-bold')
print(s)
# lines = s.find_all('h2')
# for line in lines:
#     print(line.text)

# for link in soup.find_all('a'):
#     print(link.get('href'))