from flask import Flask, redirect, url_for, render_template, request, session
from functools import wraps
app = Flask(__name__)
app.secret_key="isSecret"

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

@app.route("/signin", methods=["POST"])
def signin():
    user = request.form["user"]
    password = request.form["password"]
    if user == "test" and password == "test":
        session["loggedIn"] = True
        return redirect(url_for('.member'))
    elif user == "" or password == "":
        return redirect(url_for('.error', message="請輸入帳號、密碼")) 
    else:
        return redirect(url_for('.error', message="帳號、或密碼輸入錯誤"))

@app.route("/member")
@login
def member():
    return render_template("member.html")

@app.route("/signout")
@login
def signout():
    session.pop("loggedIn", None)
    return redirect(url_for('.home'))

@app.route("/error")
def error():
    message = request.args.get("message", "")
    return render_template("error.html", data=message)

# @app.route("/square/<int:num>")
# def square(num):
#     # num = request.args.get("num")
#     result = num**2
#     return render_template("square.html", data=result)

if __name__ == "__main__":
    app.run(port=3000, debug = True)