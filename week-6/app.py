from flask import Flask, redirect, url_for, render_template, request, session
import mysql.connector
from functools import wraps
app = Flask(__name__)
app.secret_key="isSecret"

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "website"
)

mycursor = db.cursor()

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
    name = request.form["name"]
    username = request.form['username']
    password = request.form['password']
    mycursor.execute("SELECT username FROM member WHERE username = %s", [username])
    myresult = mycursor.fetchall()
    if name =="" or username =="" or password =="":
        return redirect(url_for('.error', message="註冊帳號未填寫完整"))
    elif myresult == []:
        mycursor.execute("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)", (name, username, password))
        db.commit()
        return redirect(url_for('.home'))
    elif username == myresult[0][0]:
        return redirect(url_for('.error', message="帳號已經被註冊"))
    else:
        return redirect(url_for('.error', message="其他錯誤訊息"))

@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    mycursor.execute("SELECT username, password, name, id FROM member WHERE username = %s" , [username])
    thisMember = mycursor.fetchall()
    if username == "" or password == "":
        return redirect(url_for('.error', message="請輸入帳號、密碼")) 
    elif thisMember == []:
        return redirect(url_for('.error', message="帳號或密碼輸入錯誤"))
    elif username == thisMember[0][0] and password == thisMember[0][1]:
        session["loggedIn"] = True
        session["name"] = thisMember[0][2]
        session["id"] = thisMember[0][3]
        return redirect(url_for('.member', user=thisMember[0][2]))
    else:
        return redirect(url_for('.error', message="帳號或密碼輸入錯誤"))

@app.route("/member")
@login
def member():
    user = session.get("name")
    mycursor.execute("SELECT member.name, message.content FROM member INNER JOIN message on member.id = message.member_id;")
    message = mycursor.fetchall()
    return render_template("member.html", data=user, message=message)

@app.route("/message", methods=["POST"])
def message():
    user_id = session.get("id")
    content = request.form["content"]
    mycursor.execute("INSERT INTO message (member_id, content) VALUES (%s, %s)", (user_id, content))
    db.commit()
    return redirect(url_for('.member'))

@app.route("/signout")
@login
def signout():
    session.pop("loggedIn", None)
    return redirect(url_for('.home'))

@app.route("/error")
def error():
    message = request.args.get("message", "")
    return render_template("error.html", data=message)

# db.close()

if __name__ == "__main__":
    app.run(port=3000, debug = True)
