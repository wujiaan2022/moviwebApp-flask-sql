from flask_sqlalchemy import SQLAlchemy
from data_manager_interface import DataManagerInterface
from flask import Flask


class SQLiteDataManager(DataManagerInterface):
    def __init__(self, db_file_name):
        # Initialize Flask app
        self.app = Flask(__name__)
        # Configure the database URI
        self.app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_file_name}'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        # Initialize SQLAlchemy with the Flask app
        self.db = SQLAlchemy(self.app)
        # Create all tables (if not already created)
        with self.app.app_context():
            self.db.create_all()
