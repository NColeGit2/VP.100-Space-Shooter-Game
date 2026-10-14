

from flask import Flask, render_template, request
import sqlite3
import requests

app=Flask(__name__)

connect = sqlite3.connect('database.db')
connect.execute('CREATE TABLE IF NOT EXISTS leaderboard (username TEXT, score INTEGER)')

dataTable=[]

@app.route('/', methods=['GET', 'POST'])
def home():
    data=request.get_json()
    try:
        for (key, value) in data.items():
            print(f'key: {key} value: {value}')
            dataTable.append({key, value})
        print("apple")
        print(data)
    except:
        print(data)
    
    """
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM leaderboard')

    data = cursor.fetchall()
    return render_template('index.html', data=data)
    """
    print(dataTable)
    return render_template('index.html', data=data)

@app.route('/page2')
def page2():
    return '<h1>2</h1>'

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
