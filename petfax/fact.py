from flask import Blueprint, render_template, request, redirect
# import the models file 
from . import models

bp = Blueprint('fact', __name__, url_prefix='/facts')

@bp.route('/', methods=['GET', 'POST'])
def submit_fact():
    if request.method == 'POST':
        # create variables for submitter and fact then set them to their corresponding dictionary values
        submitter = request.form['submitter']
        fact = request.form['fact']

        # create a new instance of the Fact model, using the submitter and fact variables as arguments
        new_fact = models.Fact(submitter=submitter,fact=fact)
        # add the new_fact to the Flask-SQLAlchemy database session
        models.db.session.add(new_fact)
        # commit the database session, which will insert the data into the database
        models.db.session.commit()
        
        return redirect('/facts')  # Redirect to the facts page after submitting
    
        # access the query object on our Fact model and retrieve all() rows and save it to a variable named results
    results = models.Fact.query.all()
    
    
    return render_template('facts/index.html', facts=results)

@bp.route('/new')
def new():
    # If the request method is GET, render the fact submission page
    return render_template('facts/facts.html')


