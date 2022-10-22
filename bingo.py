from flask import Flask
from bingo_helpers import html_header, html_tail
import random

def makeSquares():
    squares = open("squares.txt").readlines()
    selections = random.sample(squares, k=24)
    selections.insert(12, "LIGHTS OUT and AWAY WE GO!!!")
    return selections

app = Flask(__name__)

@app.route('/')
def home():

    main_box = """
        <body>
            <div class="wrapper">
                {}
            </div>
        """

    
    squares = ' '.join(
        ['<div class="box box2" id="square{}" onclick="setColor(\'square{}\', \'#101010\')">{}</div>'.format(n,n,t) for n,t in enumerate(makeSquares())]
        )

    return html_header + main_box.format(squares) + html_tail
    

if __name__ == '__main__':
    app.run()