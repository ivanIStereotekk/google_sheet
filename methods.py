import gspread

# GOOGLE API
google_drive = gspread.service_account(filename="./keys/api_key.json")# подключились к гугл драйв
sheet = google_drive.open("TestTask")# открыли документ TestTask
list1 = sheet.worksheet("List1")# в документе обращаемся к вкладке ( list1 )

# получили все записи в вкладке
all_records = list1.get_all_records()
# получили все значения в ячейках таблиц
all_values = list1.get_all_values()



for row in all_records:
    print(row)