from flask import Blueprint, render_template, request

bp = Blueprint('fact', __name__, url_prefix='/facts')

@bp.route('/new', methods=['GET', 'POST'])
def submit_fact():
    if request.method == 'POST':
        # Handle form submission (to be implemented later)
        # For now, we simply return a message indicating that the fact was submitted
        return 'Fact submitted!'
    else:
        # If the request method is GET, render the fact submission page
        return render_template('facts/facts.html')

