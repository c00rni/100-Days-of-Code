"""Web scrapper of music billborad.

This module extract data from the billboard website (https://www.billboard.com/).
"""


from requests import get
from bs4 import BeautifulSoup
from datetime import datetime


class Billboard:

    def __init__(self) -> None:
        pass


    def getTop100(self, date:datetime) -> list:
        """Fetch top 100 billboard song on the of the specified date.
        
        Args:
            date:
                The date of the billboard top 100 to extract
        Returns:
            A orderered list of dict mapping the title and the artist of the songs. Songs
            are ordered from the most to the least popular.
        """
        
        request = get(f"https://www.billboard.com/charts/hot-100/{date.strftime('%Y-%m-%d')}/")
        soup = BeautifulSoup(request.text, 'html.parser')
        rows = soup.find_all("div", class_="o-chart-results-list-row-container")
        songs = []
        for row in rows:
            song_li = row.ul.find("li", class_="lrv-u-width-100p").ul.find_all("li")[0]
            songs.append({"title": song_li.h3.contents[0].strip(), "artist": song_li.span.contents[0].strip()})
        return songs