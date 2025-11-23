"User playing hangman in their browser"
"Relationship to routes_py => Sends HTTP requests to, HTTP/HTTPS"
"Relationship from routes_py - recieves feedback for the user and displays it"

from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('alphabet.html')

@app.route('/success/<name>')
def success(name):
    return f'welcome {name}'

@app.route('/A')
def A():
    return 'some text'

@app.route('/alphabet', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('A', name='Z'))
    elif request.method == 'A':
        user = request.args.get('nm')
        return redirect(url_for('A', letter='X'))



if __name__ == '__main__':
    app.run(debug=True)
"Relationship to main.py => Sends HTTP requests to, HTTP/HTTPS"
"Relationship from main.py - recieves feedback "
"for the user and displays it"

# When the user launches the app, a screen 
# loads which asks whether the user
#-wants to start a new game or to resume the existing game

def start_game():
# The user clicks to load a new game or resume existing
# The output is sent to main via the recieve_request
#  function in convertor.py
    return None

# The user is asked to make a guess

def make_aguess():
    return None

