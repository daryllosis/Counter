'''
Author: Daryll Osis
Date April 6, 2017
Description: Build a flask application that counts the number of times the root route ('/') has been viewed. also, add 
             an increment button that increments the session count by 2, and a reset button that resets the counter.
'''

from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = 'denvernuggets'
app.count = 0

@app.route('/')
def index():
    session['count'] += 1
    return render_template('index.html', count = session['count'])

@app.route('/increment', methods=['POST'])
def addTwo():
    #increment by 1 since redirecting the page will add another 1
    session['count'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def resetCounter():
    #increment by 1 since redirecting the page will add another 1
    session['count'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)