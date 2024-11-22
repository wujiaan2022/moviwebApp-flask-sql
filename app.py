from flask import Flask, request, jsonify
from datamanager.sqlite_data_manager import SQLiteDataManager

# Initialize Flask app
app = Flask(__name__)

# Configure the app
DB_FILE_NAME = "moviwebapp.db"
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_FILE_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the Data Manager
data_manager = SQLiteDataManager(DB_FILE_NAME)


@app.route("/")
def home():
    return "Welcome to the MoviWebApp!"


# Example route: Fetch all movies
@app.route("/movies", methods=["GET"])
def get_movies():
    with app.app_context():
        movies = data_manager.db.session.query(data_manager.Movie).all()
        movies_list = [
            {"id": movie.id, "title": movie.title, "year": movie.year}
            for movie in movies
        ]
        return jsonify(movies_list)


# Example route: Add a new movie
@app.route("/movies", methods=["POST"])
def add_movie():
    movie_data = request.json
    title = movie_data.get("title")
    year = movie_data.get("year")
    if not title or not year:
        return jsonify({"error": "Title and year are required"}), 400

    with app.app_context():
        new_movie = data_manager.Movie(title=title, year=year)
        data_manager.db.session.add(new_movie)
        data_manager.db.session.commit()
        return jsonify({"message": "Movie added successfully!"})


# Example route: Delete a movie
@app.route("/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    with app.app_context():
        movie = data_manager.db.session.query(data_manager.Movie).get(movie_id)
        if not movie:
            return jsonify({"error": "Movie not found"}), 404
        data_manager.db.session.delete(movie)
        data_manager.db.session.commit()
        return jsonify({"message": "Movie deleted successfully!"})


if __name__ == "__main__":
    app.run(debug=True)
