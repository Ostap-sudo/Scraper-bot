# UA NBU Exchange Rate Scraper

This is a simple manual web scraper written in Python that retrieves the official daily exchange rates from the National Bank of Ukraine (NBU) website.

## 🛠 Features

- Fetches the latest exchange rates from the [NBU exchange rate page](https://bank.gov.ua/ua/markets/exchangerates)
- Parses HTML using `BeautifulSoup`
- Prints currency data to the console
- Saves data to a CSV file (`nbu_rates.csv`) with UTF-8 encoding

## 📦 Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`

You can install dependencies via pip:

```bash
pip install requests beautifulsoup4

▶️ How to Run
Clone or download this repository.

Run the script manually:

bash
python nbu_scraper.py
The output will be displayed in the terminal and saved to a nbu_rates.csv file.

📁 Sample Output
text
Exchange Rates as of 2025-04-22:
['036', 'USD', 'US Dollar', '1', '40.2500']
['978', 'EUR', 'Euro', '1', '43.6700']
...
📄 CSV Structure

Numeric Code	Char Code	Currency Name	Units	Exchange Rate
036	USD	US Dollar	1	40.2500
978	EUR	Euro	1	43.6700
💡 Notes
The script scrapes data directly from HTML, so structure changes on the NBU site may break functionality.

You can schedule it with tools like cron (Linux/macOS) or Task Scheduler (Windows) for automatic runs.

📬 Contact
If you have any questions or suggestions, feel free to reach out.