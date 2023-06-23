
# Setting up initial install

As always you should start with an empty `venv`, activate it and install the 
required dependancys:

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

Now you can fill initalize the database with some dummy data by using `make`:

```bash
$ make database
```

Now start the app with `make` or run it manually:

```bash
$ make run
```

# Todo

- [ ] App loads slowly when using SSL
- [ ] Add code to navigate (add a menu)