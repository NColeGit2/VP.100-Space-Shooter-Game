

from flask import Flask, render_template, request
import sqlite3

app=Flask(__name__)


insertSQL='''INSERT INTO leaderboard(username,score) VALUES(?,?)'''

dataTable=[]



@app.route('/', methods=['GET', 'POST'])
def home():

    data=request.get_data()
    #fix data to values from query string thing
    try:
        data=data.decode()
        data=data.split('&')
        tempname=data[0].split('=')
        temppts=data[1].split('=')

        username=tempname[1]
        points=temppts[1]

        dataTable.append([username, points])
    except:
        print("No data to add or error i dunno")
    print(dataTable)
    for data in dataTable:
        print(data[0])
        print(data[1])
    """
    connect = sqlite3.connect('database.db')
    connect.execute('CREATE TABLE IF NOT EXISTS leaderboard (username TEXT, score INTEGER)')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM leaderboard')

    def updateLeaderboard(username, score, insertSQL):
        vals=(f'{username}',f'{score}')
        cursor.execute(insertSQL, vals)
        connect.commit()

    #
    try:
        updateLeaderboard(username, points, insertSQL)
    except:
        print("failure")
    
    dbData = cursor.fetchall()
    cursor.execute('SELECT * FROM leaderboard')
    return render_template('index.html', dbData=dbData)
    """
    return render_template('index.html', dbData=dataTable)
@app.route('/page2')
def page2():
    return '<h1>2</h1>'

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
