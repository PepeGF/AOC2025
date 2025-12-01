import os
import sys

import requests
from dotenv import load_dotenv


def read_data_web():
    load_dotenv()
    AOC_SESSION = os.getenv("session")
    print(AOC_SESSION)
    day: str = sys.argv[1]
    print("day:", day)
    url: str = f"https://adventofcode.com/2025/day/{day}/input"
    s = requests.Session()
    s.cookies.set("session", AOC_SESSION)
    response: requests.Response = s.get(url)
    print(response.status_code)
    return response.text


def read_data_file(day: str) -> str:
    with open(f"dia{day}/input.txt", "r", encoding="utf-8") as f:
        return f.read()


def save_data(day: str, data: str) -> None:
    data = read_data_web()
    with open(f"dia{day}/input.txt", "w", encoding="utf-8") as f:
        f.write(data)
