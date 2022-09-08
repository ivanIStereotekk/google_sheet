import gspread

# GOOGLE API


google_drive = gspread.service_account(filename="./keys/api_key.json")

sheet = google_drive.open("TestTask")

list1 = sheet.worksheet("List1")

col_names = list1.get('A1:D1')

all_recs = list1.get_all_records()


rub_cost = 'стоймость, RUB'

all_val = list1.get_all_values()



for row in all_val:
    print(row)