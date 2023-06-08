#Factory

#import the flask package
from flask import Flask

# define a function named create_app that will be our application factory
def create_app():
    # inside that function, create a new app instance of Flask
    app = Flask(__name__)
    # still inside the function, create a basic index route that goes to '/' and just returns 'Hello, PetFax!' as a string.

    @app.route('/')
    def hello():
        return 'Hello, PetFax!'
    
    # import the pet file
    from . import pet
    # call the register_blueprint method on the app instance and pass the pet blueprint into the method
    app.register_blueprint(pet.bp)

    # return the app instance at the end of factory
    return app
