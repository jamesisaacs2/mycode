#!/usr/bin/python3
"""RZFeeser || Alta3 Research
Tracking student inventory within a sqliteDB accessed
via Flask APIs"""

# standard library
import sqlite3 as sql

# python3 -m pip install flask
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

# return home.html (landing page)
@app.route('/')
def home():
    return render_template('home.html')

# return new.html (a way to add a student to our sqliteDB)
@app.route('/enternew')
def new_student():
    return render_template('new.html')

# if someone uses new.html it will generate a POST
# this post will be sent to /addrec
# where the information will be added to the sqliteDB
@app.route('/addrec',methods = ['POST'])
def addrec():
    try:
        nm = request.form['nm']         # student name
        addr = request.form['addr']     # student street address
        city = request.form['city']     # student city
        pin = request.form['pin']       # "pin" assigned to student
                                        # ("pin" is just an example of meta data we want to track)

        # connect to sqliteDB
        with sql.connect("database.db") as con:
            cur = con.cursor()

            # place the info from our form into the sqliteDB
            cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
            # commit the transaction to our sqliteDB
            con.commit()
        # if we have made it this far, the record was successfully added to the DB
        msg = "Record successfully added"
        
    except:
        con.rollback()  # this is the opposite of a commit()
        msg = "error in insert operation"    # we were NOT successful

    finally:
        # con.close()     # successful or not, close the connection to sqliteDB
        return render_template("resultadd.html",msg = msg)    #

# return all entries from our sqliteDB as HTML
@app.route('/list')
def list_students():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("SELECT * from students")           # pull all information from the table "students"
    
    rows = cur.fetchall()
    return render_template("view.html",rows = rows) # return all of the sqliteDB info as HTML

# use a HTTP DELETE to remove an entry from the table
@app.route('/remove', methods = ['DELETE'])
def remove():
    try:  # HTTP DELETE arrives at /remove?name=<name in DB to remove>

        name_to_remove = request.args.get("name") # peel off arguments and capture name to be removed

        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM students WHERE name=(?)",(name_to_remove,))





            data = cur.fetchall()
            if len(data) == 0:
                msg = "record does not exist"
            else:
                # place the info from our form into the sqliteDB
                cur.execute("DELETE FROM students WHERE name=(?)",(name_to_remove,) )

                # commit the transaction to our sqliteDB
                con.commit()

                # if we have made it this far, the record was successfully added to the DB
                msg = "record successfully removed"

    except:
        msg = "error in removing the record"
    finally:
        return render_template("resultadd.html",msg = msg) # return success


if __name__ == '__main__':
    try:
        # ensure the sqliteDB is created
        con = sql.connect('database.db')
        print("Opened database successfully")
        # ensure that the table students is ready to be written to
        con.execute('CREATE TABLE IF NOT EXISTS students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
        print("Table created successfully")
        con.close()
        # begin Flask Application 
        app.run(host="0.0.0.0", port=2224, debug = True)
    except:
        print("App failed on boot")

