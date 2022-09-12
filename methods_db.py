
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


def put_data_to_database():
    from g_parser import get_all_records, list1
    """
    Actually this is the periodic task, or function.
    This function interacts with google sheet > takes data > put's data to database:
    :return:
    """
    try:
        all_record = get_all_records(list1)
        container = []
        for row in all_record:
            # Making new item from all records in google sheet:
            new_Item = Item(
                id=row['№'],
                order_num=row['заказ №'],
                price_usd=row['стоимость,$'],
                rub_price=round(convert_rubles(row['стоимость,$']),2),
                delivery_data=str(row['срок поставки']),
            )
            # Query - the item which are the same as new item - returns None if item doesn't exist:
            if db_session.query(Item).filter_by(order_num=str(new_Item.order_num)).one_or_none() is None:
                container.append(new_Item)
        # end of procedures:
        for i in container:
            db_session.add(i)
            try:
                db_session.commit()
            except:
                db_session.rollback()
        db_session.commit()
        db_session.close()
        all_record = get_all_records(list1)
    except (Exception,KeyboardInterrupt):
        return f"******\nPeriodic Task Interupted By User >>>>:\n{traceback.format_exc()}"