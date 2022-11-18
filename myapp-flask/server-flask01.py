#!/usr/bin/python3

# standard library
import sqlite3 as sql

# python3 -m pip install flask
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import jsonify

app = Flask(__name__)

# json data
persondata = [{
    "name": "James",
    "realName": "Yaakov ben Yitzchak",
    "since": 1971,
    "foods": [
        "apples",
        "honey",
        "challah",
        "latkes"
    ]
}]


# endpoint to return json data
@app.route("/jason", methods=["GET", "POST"])
def jason():
    if request.method == 'POST':
        data = request.json
        if data:
            data = json.loads(data)
            name = data["name"]
            realname = data["realName"]
            since = data["since"]
            powers = data["foods"]
            persondata.append({"name": name, "realName": realname, "since": since, "foods": powers})

    return jsonify(persondata)


# return home.html (landing page)
@app.route('/')
def home():
    return render_template('home.html')


# return person.html (to add an entry to DB)
@app.route('/new')
def new_entry():
    return render_template('person.html')


# if someone uses person.html it will generate a POST
# this post will be sent to /new
# where the information will be added to the sqliteDB
@app.route('/add', methods=['POST'])
def add_new():
    try:
        nm = request.form['nm']  # name
        addr = request.form['addr']  # street address
        city = request.form['city']  # city
        id = request.form['id']  # id, unconstrained -- doesn't have to be unique

        # connect to sqliteDB
        with sql.connect("db_people.db") as con:
            cursor = con.cursor()

            # place the info from our form into the sqliteDB
            cursor.execute("INSERT INTO people (name,addr,city,id) VALUES (?,?,?,?)", (nm, addr, city, id))

            # commit the transaction to our sqliteDB
            con.commit()

        # record was successfully added to the DB
        msg = "Record successfully added"
    except:
        con.rollback()  # this undoes the commit()
        msg = "error in insert operation"  # we were NOT successful

    finally:
        # con.close()     # successful or not, close the connection to sqliteDB
        return render_template("resultadd.html", msg=msg)  # to display msg result


# return all entries from our sqliteDB as HTML
@app.route('/view')
def list_people():
    con = sql.connect("db_people.db")
    con.row_factory = sql.Row

    cursor = con.cursor()
    cursor.execute("SELECT * from people")  # pull all information from the table "people"

    rows = cursor.fetchall()
    return render_template("view.html", rows=rows)  # return all sqliteDB info as HTML


# use an HTTP DELETE to remove an entry from the table
@app.route('/delete', methods=['DELETE'])
def remove():
    try:  # HTTP DELETE arrives at /delete?name=<name in DB to remove>
        name_to_remove = request.args.get("name")  # peel off arguments and capture name to be removed

        with sql.connect("db_people.db") as con:
            cursor = con.cursor()
            cursor.execute("SELECT * FROM people WHERE name=(?)", (name_to_remove,))

            data = cursor.fetchall()
            if len(data) == 0:
                msg = "record does not exist"
            else:
                # place the info from our form into the sqliteDB
                cursor.execute("DELETE FROM people WHERE name=(?)", (name_to_remove,))

                # commit the transaction to our sqliteDB
                con.commit()

                # if we have made it this far, the record was successfully added to the DB
                msg = "record successfully removed"

    except:
        msg = "error in removing the record"

    finally:
        return render_template("resultdelete.html", msg=msg)  # return success


if __name__ == '__main__':
    try:
        # ensure the sqliteDB is created
        conn = sql.connect('db_people.db')
        print("db_people opened successfully")

        # ensure that the table people is ready to be written to
        conn.execute('CREATE TABLE IF NOT EXISTS people (name TEXT, addr TEXT, city TEXT, id TEXT)')
        print("Table created successfully")
        conn.close()

        # begin Flask Application
        app.run(host="0.0.0.0", port=2224, debug=True)

    except:
        print("App failed on boot")
