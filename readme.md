Wikipedia Scraper Script
This script uses the requests and BeautifulSoup libraries to scrape headings from the Wikipedia Main Page in Ukrainian. Every day at 10:00 AM, the bot automatically collects all headings (h1, h2, h3) and saves them into a CSV file.

How to Use
Install Dependencies

First, you need to install the required libraries if they are not installed yet:

bash
pip install requests beautifulsoup4 schedule
Run the Script

To run the script from the command line:

bash
python scraper.py
The script will start running and will execute the scraping task daily at 10:00 AM.

CSV Format

After each run, the script will create or append to a CSV file with the current date (e.g., headings_2023-04-15.csv). This file contains all the headings scraped from the Wikipedia page:

csv
Headings
Main page
Languages
Featured articles
...
How to Set Up Automatic Execution Using Windows Task Scheduler
To make the script run automatically every day at 10:00 AM, you can set up Task Scheduler in Windows.

Steps:
Create a New Task in Task Scheduler

Open Task Scheduler from the Start menu.

On the right side of the window, click Create Task.

In the General tab, enter the task name, e.g., Wikipedia Scraper.

Configure the Trigger

Go to the Triggers tab, click New, select Daily, and set the time to 10:00 AM.

Configure the Action

Go to the Actions tab, click New, and choose Start a Program.

In the Program/script field, specify the path to Python in your virtual environment (e.g., C:\path\to\your\env\Scripts\python.exe).

In the Add arguments field, specify the path to your script:

bash

C:\path\to\your\scraper.py
Save and Run

Click OK to save the task.

The task will automatically run every day at 10:00 AM, executing the script.

Notes:
Make sure your computer is powered on at the scheduled time so the script can run.

If the computer is turned off, the task will be missed, and the script won't run.

Customization
To change the URL to scrape, modify the url variable in the scrape_wikipedia() function.

You can change the CSV format or add additional sections to store data.

