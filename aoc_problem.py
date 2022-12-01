import sys
from datetime import datetime
import os
import requests
from bs4 import BeautifulSoup
import re

if __name__ == "__main__":
    if len(sys.argv) > 2:
        year = sys.argv[1]
        day = sys.argv[2]
    else:
        year = datetime.now().year
        day = datetime.now().day
    
    cookies = {"session": os.getenv("AOC_SESSION")}
    data = requests.get(f"https://adventofcode.com/{year}/day/{day}", cookies=cookies)
    soup = BeautifulSoup(data.text,features="lxml")
    content = soup.find_all("article", class_=re.compile("day-desc"))
    path = f"./{year}/{day}/"
    if not os.path.exists(f"./{year}/{day}/"):
        os.makedirs(path)
        print(f"You can start working on {year}/{day} problem")
    
    for tag in content:
        for line in tag.contents:
            print(line.text)