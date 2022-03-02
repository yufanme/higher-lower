from flask import Flask
import random
import os

app = Flask(__name__)

aim_number = random.randint(0, 9)
print(aim_number)


@app.route('/<int:user_number>')
def guess_number(user_number):
    if user_number == aim_number:
        return '<h1 style="text-align: center; color: green">You found me!</h1>' \
               '<div align="middle"><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"></div>'
    elif user_number > aim_number:
        return '<h1 style="text-align: center; color: red">Too high, try again!</h1>' \
               '<div align="middle"><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"></div>'
    else:
        return '<h1 style="text-align: center; color: blue">Too low, try again!</h1>' \
               '<div align="middle"><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"></div>'


@app.route('/')
def home_page():
    return '<h1 style="text-align: center">Guess a number between 0 and 9</h1>' \
           '<div align="middle"><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></div>'


if __name__ == "__main__":
    app.run(debug=True,
            port=int(os.getenv('PORT', 4444)))
