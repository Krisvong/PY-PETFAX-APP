# Import the 'SQLAlchemy' class from the 'flask_sqlalchemy' module
from flask_sqlalchemy import SQLAlchemy

# Create an instance of the 'SQLAlchemy' class
db = SQLAlchemy()

# Define a model class named 'Fact'
class Fact(db.Model):
    # Set the name of the database table associated with this model
    __tablename__ = 'facts'

    # Define the 'id' column as an integer primary key
    id = db.Column(db.Integer, primary_key=True)

    # Define the 'submitter' column as a string with a maximum length of 250 characters
    submitter = db.Column(db.String(250))

    # Define the 'fact' column as a text column
    fact = db.Column(db.Text)
