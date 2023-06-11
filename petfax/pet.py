# import Blueprint from flask
from flask import Blueprint, render_template 

import json
# Load pets data from JSON file
pets = json.load(open('pets.json'))
# print(pets)

# create a new instance of Blueprint and save it to a variable called bp with the required three arguments: name of blueprint:pet; location of blueprint; __name__; and the URL prefix that should be used for all routes attached to this blueprint: /pets
bp = Blueprint('pet', __name__, url_prefix="/pets")

# define a route on the blueprint instance that goes to '/'.
@bp.route('/')
#define a method for the route named index
def index():
    #in the index method, return a string
    return render_template('pets/index.html', pets=pets)

@bp.route('/<int:pet_id>') #decorator that defines the route for the show page of an individual pet. It indicates taht the route expects an integer value for the pet_id parameter.
def show(pet_id):
    # Find the pet with the given pet_id
    pet = next((p for p in pets if p['pet_id'] == pet_id), None)

    if pet:
        #If a pet with the given pet_id is found, render the new.html' template and pass the 'pet' object as a variable to the template
        return render_template('pets/new.html', pet=pet)
    else:
        # If no pet with the given pet_id is found, return a simple message indicating that the pet was not found
        return 'Pet not found'
