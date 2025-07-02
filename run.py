# from datetime import date, timedelta

# print(date.today()+timedelta(days=5))

import requests

resp = requests.get('https://google.com')
print(resp.status_code)