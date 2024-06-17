from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5


class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "rmTuXwDhKXLBCZKz5hjkMtchfTFWeV81hJi955t0H09xEU4C73TOXEJWL6VwjwLU"

bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form  = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@mail.org" and login_form.password.data == "secret":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
