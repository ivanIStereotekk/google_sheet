import datetime
import time

import gspread

# GOOGLE API
google_drive = gspread.service_account(filename="./keys/api_key.json")  # подключились к гугл драйв
sheet = google_drive.open("TestTask")  # открыли документ TestTask
list1 = sheet.worksheet("List1")  # в документе обращаемся к вкладке ( list1 )

# получили все записи в вкладке
all_records = list1.get_all_records()
# получили все значения в ячейках таблиц
all_values = list1.get_all_values()



# GET ALL RECORDS FROM GOOGLE SHEET
def get_all_records(data_sheet):
    data_sheet = data_sheet
    """
    Получаем все записи в таблице через переменную data_sheet (можно подставить другую)
    :return: all_records
    """
    _records = data_sheet.get_all_records()
    return _records


# GET ALL VALUES FROM GOOGLE SHEET
def get_all_values(data_sheet):
    data_sheet = data_sheet
    """
    Получаем все записи в таблице через переменную data_sheet (можно подставить другую)
    :return: all_values
    """
    _values = data_sheet.get_all_values()
    return _values


from datetime import datetime as tm

now = tm.now()

def make_color():
    for i in all_records:
        delivery = tm.strptime(str(i['срок поставки']), "%d.%m.%Y")
        delta  = delivery - now
        match delta.days:
                case 5:#BOLD
                    list1.format(f"D{i['№'] + 1}", {'textFormat': {'bold': True}})
                case 3:#GREEN
                    list1.format(f"D{i['№'] + 1}", {"backgroundColor": {"red": 0.0, "green": 1.0, "blue": 0.0}})
                case 1:#BLUE
                    list1.format(f"D{i['№'] + 1}", {"backgroundColor": {"red": 0.0,"green":0.0,"blue":1.0}})
                case 0:#RED
                    list1.format(f"D{i['№'] + 1}", {"backgroundColor": {"red": 1.0, "green": 0.0, "blue": 0.0}})







make_color()