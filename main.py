from flask import Flask
from models import Item
from db import Session
db_session = Session()

app = Flask(__name__)



@app.route("/")
def main_page():

    return f"<p>{db_session.query(Item).all()}</p>"



if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8000,debug=True)
