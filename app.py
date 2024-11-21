from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datamanager.sqlite_data_manager import SQLiteDataManager

# Initialize Flask app
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/moviwebapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize the SQLiteDataManager
data_manager = SQLiteDataManager(app)


@app.route('/')
def home():
    return "Welcome to MoviWebApp!"


@app.route('/users')
def list_users():
    users = data_manager.get_all_users()
    return str(users)  # Temporarily returning users as a string


if __name__ == '__main__':
    app.run(debug=True)