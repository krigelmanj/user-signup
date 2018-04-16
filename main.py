from flask import Flask, request , redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def index():
    username = ""
    username_error = 'COW'
    username = ""
    email = ""
    return render_template('base.html', username="", email="")


@app.route("/", methods=['POST'])
def verify():
    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""


    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']


    if username == "":
        username_error = "you must provide a username"
    elif len(username) < 3:
        username_error = "your username isn't long enough, it must be at least three characters long"
    elif len(username) > 20:
        username_error = "your username must be less than 20 characters"

    if password == "":
        password_error = "you must provide a password"
    elif password != verify_password:
        verify_error = "You password verification was not the same as your password. "

    if verify_password == "":
        verify_error = "you must verify your password"

    if "@" not in email or "." not in email or len(email) > 20 or len(email) < 3 or " " in email:
        email_error = "that is not a valid email"

    if username_error == "" and password_error == "" and verify_error == "" and email_error == "":
        return "You have completed your first challenge" + " " + username







    return render_template('base.html', username_error=username_error,
                           password_error=password_error,
                           verify_error=verify_error,
                           email_error=email_error,
                           username=username,
                           email=email
                           )




app.run()


