from flask import Flask, request, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True



@app.route("/register", methods=['GET'])
def register_page():
    return render_template("form.html", username="", usernameError="", password="", passwordError="", password2="", password2Error="", email="", emailError="")

@app.route("/register", methods=['POST'])
def register():
    username = cgi.escape(request.form['username'])
    password = cgi.escape(request.form['password'])
    password2 = cgi.escape(request.form['password2'])
    email = cgi.escape(request.form['email'])

    username_error = ""
    password_error = ""
    password2_error = ""
    email_error = ""

    if not username:
        username_error = "Error! Not a valid username."
    if not password:
        password_error = "Error! Not a valid password."
    elif len(password) < 3:
        password_error = "Your password needs to be over 3 characters."
    if password2 != password:
        password2_error = "Your passwords must match."   
    #if not email:
        #email_error = "Error! Not a valid email."
    if "@" and "." not in email:
        email_error = "Error! Not a valid email."
    if username_error or password_error or password2_error or email_error:
        return render_template("form.html", username=username, usernameError=username_error, password=password, passwordError=password_error, password2=password2, password2Error=password2_error, email=email, emailError=email_error)

    return "Welcome, " + username
    #return render_template("form.html", title=title)

@app.route("/")
def index():
    return render_template('form.html', title="User Signup")
    

app.run()
