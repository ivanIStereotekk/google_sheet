import requests
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)
CURRENCY = os.getenv("CURRENCY")


#
# Тут получили курс доллара по курсу центробанка используем функцию ниже.
#  --- convert_roubles()
import traceback
def convert_rubles(usd_sum):
    """
    Gets from TZENTROBANK API current value of RU currency then transits to roubles:
    :param usd_sum:
    :return:
    """
    try:
        response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        all_json = response.json()
        parsed = all_json["Valute"][CURRENCY]
        cur_value = parsed['Value']
        result = int(usd_sum) * cur_value
        return result
    except BaseException:
        return f"******\n\n\nConverter Error >>>>:\n\n\n{traceback.format_exc()}"


pasi = 95000
res = convert_rubles(str(pasi))

print(int(res))


