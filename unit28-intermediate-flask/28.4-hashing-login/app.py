from flask import Flask, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import User, connect_db, db
from forms import RegisterForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jY*j9t79Jhf8'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flask_feedback'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    """Home page"""

    return redirect("register")

@app.route("/register", methods=["GET", "POST"])
def register_user():
    """Show Registration form and handle submission of form.

    Accepts username, password, email, first name, and last name
    """

    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        
        new_user = User.register(username, password, email, first_name, last_name)
        db.session.add(new_user)
        db.session.commit()

        flash('Your account has been created')
        return redirect("/secret")
    return render_template("register.html", form=form)

@app.route('/login', methods=["GET", "POST"])
def login_user():
    """Show login form and handle user authentiction"""

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        authenticate = User.authenticate(username, password)
        if authenticate:
            return redirect('/secret')
        else:
            flash('Incorrect username or password. Please try again')
            return redirect('/login')

    return render_template('login.html', form=form)

@app.route('/secret')
def secret_page():
    return render_template('secret.html')

