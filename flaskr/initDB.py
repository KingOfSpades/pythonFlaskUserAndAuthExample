from models import User, DinnerParty
from app import app, db

# Create the inital DB
with app.app_context():
    db.create_all()

# # Create some users

# # Add the objects to a session
# with app.app_context():
#   db.session.add(todo_one)

#   # Write the session to the database
#   db.session.commit()
