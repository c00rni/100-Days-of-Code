from datetime import datetime
from requests import get
from bs4 import BeautifulSoup

date = None
date_format = "%Y-%m-%d"
"""while not date:
    try:
        user_text_input = input(f"Which yeaf do you want to travel to ? type the date in this format YYYY-MM-DD: ")
        date = datetime.strptime(user_text_input, date_format)
    except ValueError:
        pass"""

date = datetime(year=1990, month=2, day=1)
request = get(f"https://www.billboard.com/charts/hot-100/{date.strftime(date_format)}/")
soup = BeautifulSoup(request.text, 'html.parser')
rows = soup.find_all("div", class_="o-chart-results-list-row-container")
for row in rows:
    song_li = row.ul.find("li", class_="lrv-u-width-100p").ul.find_all("li")[0]
    print(song_li.h3.contents[0].strip())
    print(song_li.span.contents[0].strip())
    print("#############")