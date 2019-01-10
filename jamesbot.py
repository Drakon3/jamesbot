from flask import Flask, request
app = Flask(__name__)



@app.route('/greet', methods=['GET', 'POST'])
def greet_person():
    name = request.values.get('text')
    return f'Greetings {name}!'

"""@app.route('/', methods = ['GET', 'POST'])
def :"""


if __name__ == '__main__':
    app.run()

#this is a comment