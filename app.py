from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmyql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_spauldmi'
app.config['MYSQL_PASSWORD'] = '5854'
app.config['MYSQL_DB'] = 'cs_spauldmi'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


# Routes
@app.route('/')
def root():
    query = "SELECT * FROM diagnostic;"
    query1 = 'DROP TABLE IF EXISTS diagnostic;';
    query2 = 'CREATE TABLE diagnostic(id INT PRIMARY KEY AUTO_INCREMENT, text VARCHAR(255) NOT NULL);';
    query3 = 'INSERT INTO diagnostic (text) VALUES ("MySQL is working!")';
    query4 = 'SELECT * FROM diagnostic;';
    cur = mysql.connection.cursor()
    cur.execute(query1)
    cur.execute(query2)
    cur.execute(query3)
    cur.execute(query4)
    results = cur.fetchall()

    return "<h1>MySQL Results</h1>" + str(results[0])


# Listener
if __name__ == '__main__':
    app.run(port=3000, debug=True)
