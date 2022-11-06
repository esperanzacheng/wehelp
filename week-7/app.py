import mysql.connector
import json
import requests

from flask import Flask, redirect, url_for, render_template, request, session, request
from functools import wraps

app = Flask(__name__)
app.secret_key="isSecret"

connection_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name = "week7_pool",
    pool_size = 5,
    pool_reset_session = True,
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "website"
)

def login(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if "loggedIn" in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('.home'))
    return wrap

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup", methods=["POST"])
def signup():
    try:
        connection_object = connection_pool.get_connection()
        my_cursor = connection_object.cursor()
        name = request.form["name"]
        username = request.form['username']
        password = request.form['password']
        my_cursor.execute("SELECT username FROM member WHERE username = %s", [username])
        my_result = my_cursor.fetchone()
        if name =="" or username =="" or password =="":
            return redirect(url_for('.error', message="註冊帳號未填寫完整"))
        elif my_result == None:
            my_cursor.execute("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)", (name, username, password))
            connection_object.commit()
            return redirect(url_for('.home'))
        elif username == my_result[0]:
            return redirect(url_for('.error', message="帳號已經被註冊"))
        else:
            return redirect(url_for('.error', message="其他錯誤訊息"))
    finally:
        my_cursor.close()
        connection_object.close()

@app.route("/signin", methods=["POST"])
def signin():
    try:
        connection_object = connection_pool.get_connection()
        my_cursor = connection_object.cursor()
        username = request.form["username"]
        password = request.form["password"]
        my_cursor.execute("SELECT username, password, name, id FROM member WHERE username = %s" , [username])
        this_member = my_cursor.fetchone()
        if username == "" or password == "":
            return redirect(url_for('.error', message="請輸入帳號、密碼")) 
        elif this_member == []:
            return redirect(url_for('.error', message="帳號或密碼輸入錯誤"))
        elif username == this_member[0] and password == this_member[1]:
            session["loggedIn"] = True
            session["name"] = this_member[2]
            session["id"] = this_member[3]
            return redirect(url_for('.member', user=this_member[2]))
        else:
            return redirect(url_for('.error', message="帳號或密碼輸入錯誤"))
    finally:
        my_cursor.close()
        connection_object.close()

@app.route("/member")
@login
def member():
    try:
        connection_object = connection_pool.get_connection()
        my_cursor = connection_object.cursor()
        user = session.get("name")
        my_cursor.execute("SELECT member.name, message.content FROM member INNER JOIN message on member.id = message.member_id;")
        message = my_cursor.fetchall()
        return render_template("member.html", data=user, message=message)
    finally:
        my_cursor.close()
        connection_object.close()

@app.route("/message", methods=["POST"])
def message():
    try:
        connection_object = connection_pool.get_connection()
        my_cursor = connection_object.cursor()
        user_id = session.get("id")
        content = request.form["content"]
        my_cursor.execute("INSERT INTO message (member_id, content) VALUES (%s, %s)", (user_id, content))
        connection_object.commit()
        return redirect(url_for('.member'))
    finally:
        my_cursor.close()
        connection_object.close()

@app.route("/api/member", methods=["GET"])
def member_search():
    try:
        username = request.args.get("username")
        connection_object = connection_pool.get_connection()
        my_cursor = connection_object.cursor()
        my_cursor.execute("SELECT id, name, username FROM member WHERE username = %s", [username])
        search_result = my_cursor.fetchone()
        data = {
            "data":{
                "id": search_result[0],
                "name": search_result[1],
                "username": search_result[2]
            }
        }
    except:
        data = {
            "data": None
        }
    finally:
        my_cursor.close()
        connection_object.close()

    return data

@app.route("/api/member", methods=["PATCH"])
def update_name():
    try:
        update_name = request.json["name"]
        user_id = session.get("id")
        connection_object = connection_pool.get_connection()
        my_cursor = connection_object.cursor()
        my_cursor.execute("UPDATE member SET name = %s WHERE id = %s", (update_name, user_id))
        connection_object.commit()
        data = {
            "ok":True
        }
    except:
        data = {
            "error":True
        }
        print("enter to except")
    finally:
        my_cursor.close()
        connection_object.close()
        return data

@app.route("/signout")
@login
def signout():
    session.pop("loggedIn", None)
    return redirect(url_for('.home'))

@app.route("/error")
def error():
    message = request.args.get("message", "")
    return render_template("error.html", data=message)

if __name__ == "__main__":
    app.run(port=3000, debug = True)
