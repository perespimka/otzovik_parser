import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding' : 'gzip, deflate, br',
'Accept-language' : 'ru,en-US;q=0.9,en;q=0.8',
'Cache-Control' : 'no-cache',
'Cookie': 'refreg=https%3A%2F%2Fotzovik.com%2Freviews%2Fbukmekerskaya_kontora_liga_stavok%2F; ssid=162305530; ownerid=01d2ff67f1a6d0a1c066049ad2aad4; referal=1; ROBINBOBIN=e352db6dlh3da2484vsl84gtc3',
'Pragma' : 'no-cache',
'Upgrade-Insecure-Requests': '1',
'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

def get_review_data(url):
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.content, 'html.parser')

    bookmaker = 'Лига Ставок'
    review_source = 'Otzovik.com'

    user_name = soup.find('img', class_='photo')['alt']

    text = soup.find('div', class_='review-body description').text.replace('"', '""') # Для вывода в CSV меняем кавычки на двойные кавычки
    date = soup.find('abbr', class_='value')['title']
    rating = soup.find('abbr', class_='rating')['title']
    plus = soup.find('div', class_='review-plus').text.replace('"', '""')
    minus = soup.find('div', class_='review-minus').text.replace('"', '""')
    text_mod = 'Плюсы: {} Минусы: {} Комментарий: {}'.format(plus, minus, text)
    # Добавляем кавычки для строк, в которых могут содержаться запятые
    return (', ').join((bookmaker, '"'+text_mod+' "', date, rating, review_source, user_name, '" '+plus+' "', '" '+minus+' "' ))



req = requests.get('https://otzovik.com/reviews/bukmekerskaya_kontora_liga_stavok/', headers=headers)
soup = BeautifulSoup(req.content, 'html.parser')

all_links = [] #Линки на отзывы

while True:
    links = [i['href'] for i in soup.find_all('a', class_='review-title')] #Собираем ссылки на отзывы на этой странице
    all_links.extend(links)

    next_page = soup.find('a', class_='pager-item next tooltip-top') #Линк на следующую страницу с отзывами
    if next_page:
        req = requests.get('https://otzovik.com' + next_page['href'], headers=headers)
        soup = BeautifulSoup(req.content, 'html.parser')
    else:
        break
'''
print(all_links)
for link in all_links:

    sleep(1)
    print(get_review_data(link) + '\n')

'''
with open('result.csv', 'w') as f:
    for link in all_links:

        sleep(2)
        f.write(get_review_data(link) + '\n')
