import requests
from bs4 import BeautifulSoup

url = "https://rugcheck.xyz/tokens/G3q2zUkuxDCXMnhdBPujjPHPw9UTMDbXqzcc2UHM3jiy"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())