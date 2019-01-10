from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/ncss')
def hello_ncss():
    return 'Yay!'

@app.route('/greet')
def greet_person():
    name = request.values.get('name')
    return f'Greetings {name}!'

@app.route('/weather')
def weather():
    temp = int(request.values.get('temp'))
    if temp > 30:
        return "It's so hot!"
    else:
        return f"The temprature is {temp}"

if __name__ == '__main__':
    app.run()

#this is a comment