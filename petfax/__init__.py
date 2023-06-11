#Factory

#import the flask package
from flask import Flask
from flask_migrate import Migrate

# define a function named create_app that will be our application factory
def create_app():
    # inside that function, create a new app instance of Flask
    app = Flask(__name__, template_folder='templates')
    # still inside the function, create a basic index route that goes to '/' and just returns 'Hello, PetFax!' as a string.

    # database config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Ardilla0103!@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Import the 'models' module
    from . import models
    # Initialize the database with the Flask 'app' instance
    models.db.init_app(app)
    # Create an instance of the 'Migrate' class, passing the Flask 'app' instance and the database instance ('models.db')
    migrate = Migrate(app, models.db)

    #index route
    @app.route('/')
    def hello():
        return 'Hello, PetFax!'
    
    # register pet blueprint
    from . import new
    # call the register_blueprint method on the app instance and pass the pet blueprint into the method
    app.register_blueprint(new.bp)

    # register fact bluprint
    from . import fact
    app.register_blueprint(fact.bp)

    # return the app instance at the end of factory
    return app
