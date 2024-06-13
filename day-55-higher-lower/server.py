from random import randint

from flask import Flask

app = Flask(__name__)

number = randint(0, 9)


@app.route('/')
def main():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXhhdm9yM3EwM3Y5ejV0eno3bTV6cW9jeDBvZGl5c3Z5amN0cGd0eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IsfrRWvbUdRny/giphy.gif" '
            'width="200">')


@app.route('/<int:guess>')
def guess_number(guess):
    if guess == number:
        msg = ('<h1>Your guess correct</h1>'
               '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGR4eXV6emh0M3prYzlncHVsNno4NnllM2s1d21wNGdxNmFkaWd4ZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/XE8iJs1sT7xTM5lafa/giphy.gif"'
               'width="200">')
    elif guess < number:
        msg = ('<h1>Your guess is to low, try again</h1>'
               '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExOTkzOGtraHoydW91ZnpldmZqMTM4bzlya2l3Zmd6a2N3ejYwbmxxciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/BEob5qwFkSJ7G/giphy.gif"'
               'width="200">')
    else:
        msg = ('<h1>Your guess is to high, try again</h1>'
               '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExOTkzOGtraHoydW91ZnpldmZqMTM4bzlya2l3Zmd6a2N3ejYwbmxxciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/BEob5qwFkSJ7G/giphy.gif"'
               'width="200">')
    return msg


if __name__ == "__main__":
    app.run(debug=True)
