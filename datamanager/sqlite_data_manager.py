from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from data_manager_interface import DataManagerInterface

# Define the declarative base for ORM models
Base = declarative_base()


class SQLiteDataManager(DataManagerInterface):
    def __init__(self, db_file_name):
        """
        Initialize SQLiteDataManager with a database file name.
        - Creates an engine, session factory, and ensures tables are created.
        """
        # Create an engine with the SQLite database file
        self.engine = create_engine(f"sqlite:///{db_file_name}", echo=True)

        # Create a session factory bound to the engine
        self.Session = sessionmaker(bind=self.engine)

        # Ensure tables defined in Base are created
        Base.metadata.create_all(self.engine)

    def get_session(self):
        """
        Create and return a new session instance.
        """
        return self.Session()

    @staticmethod
    def close_session(self, session):
        """
        Close the given session.
        """
        session.close()
