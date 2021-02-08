import requests
import json
import random
from time import sleep
from scrapic import Scrapic

scrapic = Scrapic()
for i in range(100):
    sleep(1)
    a = [
        'http://worldtimeapi.org/api/timezone/Europe/London',
        'http://worldtimeapi.org/api/timezone/Europe/Moscow'
    ]

    rand = a[random.randint(0, 1)]
    result = scrapic.closure(rand, lambda: requests.get(rand), 10)
    result = json.loads(result.text)
    print(rand, result['datetime'])
