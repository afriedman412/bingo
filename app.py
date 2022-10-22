from flask import Flask, render_template
from dotenv import load_dotenv
import random

app = Flask(__name__)
load_dotenv()
squares = open("static/squares.txt").readlines()

def make_squares(squares=squares):
    selections = random.sample(squares, k=24)
    selections.insert(12, "LIGHTS OUT and AWAY WE GO!!!")
    return selections

@app.route('/')
def home():
    select_squares = make_squares()
    return render_template("home.html", squares=select_squares)
    
if __name__ == '__main__':
    app.run()