import requests
import sys
from dotenv import load_dotenv
import os

load_dotenv()
AOC_SESSION = os.getenv("session")


def read_data():
    day = sys.argv[1]
    url = f"https://adventofcode.com/2025/day/{day}/input"
    s = requests.Session()
    s.cookies.set("session", AOC_SESSION)
    response = s.get(url)
    return response.text