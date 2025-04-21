import requests
from bs4 import BeautifulSoup
import schedule
import time
import csv
from datetime import datetime


# Функція для скрейпінгу
def scrape_wikipedia():
    url = "https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    # Виконання запиту
    response = requests.get(url, headers=headers)

    # Перевірка статусу відповіді
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Знаходимо всі заголовки секцій (наприклад, h1, h2, h3)
        headings = soup.find_all(['h1', 'h2', 'h3'])

        # Формуємо список заголовків
        headings_list = []
        for heading in headings:
            headings_list.append(heading.text.strip())

        # Записуємо заголовки у CSV
        save_to_csv(headings_list)
    else:
        print("Помилка при запиті")


# Функція для збереження результату в CSV
def save_to_csv(data):
    # Отримуємо поточну дату для формування унікального імені файлу
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"headings_{date_str}.csv"

    # Перевірка, чи існує файл. Якщо так, відкриваємо для дозапису, якщо ні — створюємо новий.
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Якщо файл порожній, додаємо заголовок
        if file.tell() == 0:
            writer.writerow(["Заголовки"])

        # Записуємо дані
        for item in data:
            writer.writerow([item])

    print(f"Дані збережено в файл {filename}")


# Функція для планування виконання бота щодня о 10:00
def job():
    print("Запуск скрейпера...")
    scrape_wikipedia()


# Плануємо запуск бота щодня о 10:00
schedule.every().day.at("10:00").do(job)

# Основний цикл, щоб бот працював постійно
while True:
    schedule.run_pending()  # Виконуємо заплановані завдання
    time.sleep(1)  # Спимо 1 секунду, щоб зменшити навантаження на процесор
