from sqlite_data_manager import SQLiteDataManager

# Access the db object from SQLiteDataManager
data_manager = SQLiteDataManager("movies.db")
db = data_manager.db

# Define the User model
class User(db.Model):
    __tablename__ = 'users'  # Optional: explicitly name the table
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier
    name = db.Column(db.String(100), nullable=False)  # User's name

    def __repr__(self):
        return f"<User {self.id}: {self.name}>"

# Define the Movie model
class Movie(db.Model):
    __tablename__ = 'movies'  # Optional: explicitly name the table
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier
    name = db.Column(db.String(200), nullable=False)  # Movie's name
    director = db.Column(db.String(100), nullable=False)  # Movie's director
    year = db.Column(db.Integer, nullable=False)  # Year of release
    rating = db.Column(db.Float, nullable=False)  # Movie rating (e.g., 8.5)

    def __repr__(self):
        return f"<Movie {self.id}: {self.name} ({self.year})>"
