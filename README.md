I was learning to work with Flask, SQLAlchemy and WTForms and Login Manager. So 
I created this simple auth app as reference to my future self and starting point 
for new apps. This example can be easily expanded to add new functions.

# Setting up initial install

Let's start by cloning this repo:

```bash
$ git clone https://github.com/KingOfSpades/...
$ cd pythonFlaskUserAndAuthExample
```

As always you should start with an empty `venv`, activate it and install the 
required dependancys:

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

Now start the app with `make` or run it manually:

```bash
$ make run
```

This will start the app on: https://127.0.0.1:5000. You will get an https error
because we are using a custom certificate. After accepting this you should see
a message that you should login. Follow the instuctions and crate an account. You
can now login to the application.


# Explaining the app

This is easy app tha relies on one (1) database model, a FlaskForm and a couple 
of routes.

The most important thing is that you need to be logged in to view the "backend".
This is handeld by `LoginManager`. Users are stored in the DB with a hashed
password using the `generate_password_hash()` method (see `models.py`).


# Forms

We use two (2) simpel forms:

- A registration form (for creating new users)
- A login form (for login in to the app)

# Neat things

A few nice things:

## Clean app.py

The `app.py` is verry _clean_ because we use the import method:

```python
# app.py
...
import routes, models
...
```

## Using SSL

This is enabled in `app.py`:

```python
# app.py
# This will create an ad hoc cert
if __name__ == "__main__":
  app.run(ssl_context='adhoc')
```

You can also choose to create a custom certificate and parse that to the app. See
https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https

You can re-direct traffic to HTTPS in routes using:

```python
# routes.py
...
return redirect(next_page) if next_page else redirect(url_for('index', _external=True, _scheme='https'))
...
```