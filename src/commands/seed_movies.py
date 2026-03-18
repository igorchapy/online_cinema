from app.models import Movie, Genre
from app.database import db_session

def run():
    # Add default genres
    genres = ["Action", "Comedy", "Drama"]
    for name in genres:
        db_session.add(Genre(name=name))
    db_session.commit()
