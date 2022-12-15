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
    pycode = f"""from aoc_lib.aoc_read_input import read_input

if __name__ == "__main__":
    data = read_input({year}, {day})
    """
    cookies = {"session": os.getenv("AOC_SESSION")}
    data = requests.get(f"https://adventofcode.com/{year}/day/{day}", cookies=cookies)
    input_data = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input", cookies=cookies
    ).text
    soup = BeautifulSoup(data.text, features="lxml")
    content = soup.find_all("article", class_=re.compile("day-desc"))
    path = f"./{year}/{day}/"
    if not os.path.exists(f"./{year}/{day}/"):
        os.makedirs(path)
        open(path + "test.in", "a").close()
        open(
            f"src/main/resources/aoc{year}/" + f"Day{day.zfill(2)}test.in", "a"
        ).close()
        open(f"src/main/resources/aoc{year}/" + f"Day{day.zfill(2)}.in", "a").write(
            input_data
        )
        print(f"You can start working on {year}/{day} problem")

    for tag in content:
        for line in tag.contents:
            print(line.text)
