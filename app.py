from . import routes
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize the Flask application
app = Flask(__name__)

# Load the configuration from the 'config.py' file
app.config.from_object('config')

# Initialize SQLAlchemy and Flask-Login
db = SQLAlchemy(app)
login_manager = LoginManager(app)

# Import the routes from the 'routes' module

# This is only true when the script is run directly, i.e. "python app.py"
if __name__ == "__main__":
    app.run(debug=True)
