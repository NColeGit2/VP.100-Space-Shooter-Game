from flask import Flask, render_template
import sqlite3

app=Flask(__name__)

connect = sqlite3.connect('database.db')
connect.execute('CREATE TABLE IF NOT EXISTS leaderboard (username TEXT, score INTEGER)')

@app.route('/')
def home():
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM leaderboard')

    data = cursor.fetchall()
    return render_template('index.html', data=data)

@app.route('/page2')
def page2():
    return '<h1>page2</h1>'

if __name__=='__main__':
    app.run(debug=True)