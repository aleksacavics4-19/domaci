from flask import Flask, render_template,redirect, url_for, request, session
from bson import ObjectId
from datetime import datetime
import hashlib
import time
import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="domaci67"
)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'januar2020'


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/raspored')
def raspored():
	mc= mydb.cursor()
	mc.execute("SELECT * FROM raspored")
	celi = mc.fetchall()

	nastavnici = []
	ucionice = []
	for i in celi:
		if i[7] not in ucionice:
			ucionice.append(i[7])

	for i in celi:
		if i[3] not in nastavnici:
			nastavnici.append(i[3])


	return render_template("baza.html", celi = celi, nastavnici = nastavnici, ucionice = ucionice)



if __name__ == '__main__':
	app.run(debug=True)