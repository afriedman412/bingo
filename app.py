from flask import Flask, render_template
from dotenv import load_dotenv
import random

app = Flask(__name__)
load_dotenv()
squares = open("static/squares.txt").readlines()

def make_squares(seed=None, squares=squares):
    if seed:
        random.seed(seed)
    selections = random.sample(squares, k=24)
    selections.insert(12, "LIGHTS OUT and AWAY WE GO!!!")
    return selections

@app.route('/')
@app.route('/<seed>')
def home(seed=None):
    if not seed:
        seed = random.randrange(100, 1000000000)
    select_squares = make_squares(seed)
    return render_template("home.html", seed=seed, squares=select_squares)
    
if __name__ == '__main__':
    app.run()