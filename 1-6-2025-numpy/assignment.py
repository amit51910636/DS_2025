# https://api.nobelprize.org/v1/prize.json


# task : which year got how many prizes

# total number of prizes per year

import json
import numpy as np

with open("prize.json", "r", encoding="utf-8") as file:
    data = json.load(file)

