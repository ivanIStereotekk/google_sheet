import schedule
# .env issues
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# PARAMETERS FROM .env
PARSING_PERIOD = os.getenv("PARSING_PERIOD")

# TASKS
from methods_db import *


def task_1():
    """
    Task imported from module methods_db.py
    gets data from google table then puts to database
    :return:
    SETINGS:
    schedule.every(10).seconds.do(job)
    schedule.every(10).minutes.do(job)
    schedule.every().hour.do(job)
    schedule.every().day.at("10:30").do(job)
    schedule.every(5).to(10).minutes.do(job)
    schedule.every().monday.do(job)
    schedule.every().wednesday.at("13:15").do(job)
    schedule.every().minute.at(":17").do(job)
    """
    put_data_to_database()


if __name__ == "__main__":
    """
    PARSING_PERIOD - seconds (.env )
    RUN COMMAND: - $python scheduler.py
    """
    schedule.every(int(PARSING_PERIOD)).seconds.do(task_1)
    while True:
        schedule.run_pending()


