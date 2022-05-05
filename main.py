import requests
from bs4 import BeautifulSoup
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
}

response = requests.get('https://www.target.com/c/grocery/-/N-5xt1a')

# Get Everything from the Page
soup = BeautifulSoup(response.content, 'lxml')

productlist = soup.find_all('ul', class_='styles__StyledRow-sc-1nuqtm0-0 bjPqBX styles__StyledRow-sc-1tk9lto-7 kgPjnW')

productlinks = []

# For loop that gathers all url links for categories
for item in productlist:
    for link in item.find_all('a', href=True):
        productlinks.append(link['href'])

print(productlinks)
