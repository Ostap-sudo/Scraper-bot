import requests
from bs4 import BeautifulSoup
import csv
from datetime import date

# URL з курсами валют НБУ
url = 'https://bank.gov.ua/ua/markets/exchangerates'

# Отримуємо HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Знаходимо таблицю з курсами валют
table = soup.find('table')

# Отримуємо заголовки таблиці
headers = [th.text.strip() for th in table.find_all('th')]

# Отримуємо дані рядків
rows = []
for tr in table.find_all('tr')[1:]:
    cols = [td.text.strip() for td in tr.find_all('td')]
    if cols:
        rows.append(cols)

# Виводимо дані у консоль
print(f"Курси валют НБУ на {date.today()}:")
for row in rows:
    print(row)

# Зберігаємо у CSV (опціонально)
with open('nbu_rates.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print("Дані збережено у файл nbu_rates.csv")