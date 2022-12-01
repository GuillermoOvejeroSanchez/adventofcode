import requests
import os
from pyfiglet import Figlet
from bs4 import BeautifulSoup
import re
from datetime import datetime
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        year = sys.argv[1]
    else:
        year = datetime.utcnow().year
    cookies = {"session": os.getenv("AOC_SESSION")}
    data = requests.get(f"https://adventofcode.com/{year}", cookies=cookies)

    soup = BeautifulSoup(data.text, features="lxml")
    output = []
    
    content = soup.find_all("span", class_=re.compile("calendar-day\d"))
    for line in content:
        output.append(line.text)

    content_completed = soup.find_all("a", class_=re.compile("calendar-day\d"))
    for line in content_completed:
        output.append(line.text)


    f = Figlet(font="slant")
    print(f.renderText(f"Advent of code"))
    [print(x) for x in output]