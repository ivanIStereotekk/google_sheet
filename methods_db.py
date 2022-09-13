
from curency import convert_rubles
import traceback
# DB Issues
from models import Item
from db import Session
# .env issues
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# PARAMETERS FROM .env
PARSING_PERIOD = os.getenv("PARSING_PERIOD")


db_session = Session()


def renew_database():
    """
    Actually this is the periodic task, or function.
    This function interacts with google sheet > takes data > put's data to database:
    :return:
    """
    from g_parser import get_all_records, list1
    container = []
    try:
        all_record = get_all_records(list1)
        for row in all_record:
            new_Item = Item(
                #id=row['№'],
                order_num=row['заказ №'],
                price_usd=row['стоимость,$'],
                rub_price=round(convert_rubles(row['стоимость,$']),2),
                delivery_data=str(row['срок поставки']),
            )
            container.append(new_Item)
        try:
            db_session.execute('delete from row_in_sheet')
            db_session.commit()
        except:
            db_session.rollback()
        for i in container:
            db_session.add(i)
            db_session.commit()
            db_session.close()
        all_record = get_all_records(list1)
        print('success')
    except (Exception, KeyboardInterrupt):
        return f"******\nPeriodic Task Interupted By User >>>>:\n{traceback.format_exc()}"
