from app import app, db, login_manager
from flask import request, render_template, flash, redirect,url_for
from models import User, DinnerParty
from flask_login import current_user, login_user, logout_user, login_required
from forms import RegistrationForm,LoginForm, DinnerPartyForm, RsvpForm
from werkzeug.urls import url_parse

# registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm(csrf_enabled=False)
  if form.validate_on_submit():
    user = User(username=form.username.data, email=form.email.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
  return render_template('register.html', title='Register', form=form)

# user loader
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

# login route
@app.route('/login', methods=['GET','POST'])
def login():
  form = LoginForm(csrf_enabled=False)
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and user.check_password(form.password.data):
      login_user(user, remember=form.remember.data)
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('index', _external=True, _scheme='https'))
    else:
      return redirect(url_for('login', _external=True, _scheme='https'))
  return render_template('login.html', form=form)


@login_manager.unauthorized_handler
def unauthorized():
  # do stuff
  return "Sorry you must be logged in to view this page <a href=/login>Login here</a>"

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# landing page route
@app.route('/')
@login_required
def index():
  current_users = User.query.all()
  return render_template('landing_page.html', current_users = current_users)
