import schedule
from curency import convert_rubles
import traceback
# DB Issues
from models import Item
from db import Session
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# PARAMETERS FROM .env
PARSING_PERIOD = os.getenv("PARSING_PERIOD")


db_session = Session()

def put_data_to_database():
    """
    Actually this is the periodic task, or function.
    This function interacts with google sheet > takes data > put's data to database:
    :return:
    """
    try:
        from g_parser import get_all_records,list1
        all_record = get_all_records(list1)
        for row in all_record:
            print(row.order_num,'--- row')
            # Making new item from all records in google sheet:
            new_Item = Item(
                order_num=row['заказ №'],
                price_usd=row['стоимость,$'],
                rub_price=round(convert_rubles(row['стоимость,$']),2),
                delivery_data=str(row['срок поставки']),
            )
            print(row.order_num,'order')
            try:
                same_Item = db_session.query(Item).filter(Item.order_num == new_Item.order_num).all()
                for item in same_Item:
                    item.order_num=row['заказ №'],
                    item.price_usd=row['стоимость,$'],
                    item.rub_price=round(convert_rubles(row['стоимость,$']),2),
                    item.delivery_data=str(row['срок поставки'])
                    print("re-recorded")
                db_session.commit()
                print(f"Item with order_num: {same_Item[0].order_num} updated:")
            except:
                try:
                    db_session.add(new_Item)
                    db_session.commit()
                    print('Commited new Item >>>>>',new_Item.order_num)
                except:
                    db_session.rollback()
                    db_session.close()
        #renew
        db_session.rollback()
        db_session.close()
        print("<<< DISCONNECTED DB:")
        all_record = get_all_records(list1)
    except (Exception,KeyboardInterrupt):
        return f"******\nPeriodic Task Interupted By User >>>>:\n{traceback.format_exc()}"

if __name__ == "__main__":
    """
    PARSING_PERIOD - seconds (.env )
    RUN COMMAND: - $python scheduler.py
    """
    schedule.every(int(PARSING_PERIOD)).seconds.do(put_data_to_database)
    while True:
        schedule.run_pending()


