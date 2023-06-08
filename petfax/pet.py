# import Blueprint from flask
from flask import ( Blueprint, render_template )

import json
# open() the pets.json file by passing it as an argument
pets = json.load(open('pets.json'))
print(pets)

# create a new instance of Blueprint and save it to a variable called bp with the required three arguments: name of blueprint:pet; location of blueprint; __name__; and the URL prefix that should be used for all routes attached to this blueprint: /pets
bp = Blueprint('pet', __name__, url_prefix="/pets")

# define a route on the blueprint instance that goes to '/'.
@bp.route('/')
#define a method for the route named index
def index():
    #in the index method, return a string
    return render_template('index.html', pets=pets)