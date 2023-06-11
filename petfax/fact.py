from flask import Blueprint, render_template, request, redirect

bp = Blueprint('fact', __name__, url_prefix='/facts')

@bp.route('/', methods=['GET', 'POST'])
def submit_fact():
    if request.method == 'POST':
        print(request.form)  # Print the submitted form data for testing
        return redirect('/facts')  # Redirect to the facts page after submitting
    
       
    return render_template('facts/index.html')

@bp.route('/new')
def new():
    # If the request method is GET, render the fact submission page
    return render_template('facts/facts.html')


