from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from .database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    description = Column(String)
    rating = Column(Float, default=0.0)
    release_year = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

def test_add_movie_to_favorites_success(client, db_session, test_user):
    movie = Movie(title="Inception", genre="Action", rating=8.8, release_year=2010)
    db_session.add(movie)
    db_session.commit()

    response = client.post(f"/favorites/{movie.id}", headers={"Authorization": f"Bearer {test_user.token}"})
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Movie added to favorites"

def test_add_movie_already_in_favorites(client, db_session, test_user):
    movie = Movie(title="Inception", genre="Action", rating=8.8, release_year=2010)
    db_session.add(movie)
    db_session.commit()


    client.post(f"/favorites/{movie.id}", headers={"Authorization": f"Bearer {test_user.token}"})
    response = client.post(f"/favorites/{movie.id}", headers={"Authorization": f"Bearer {test_user.token}"})
    assert response.status_code == 400
    data = response.json()
    assert data["error"] == "Movie already in favorites"

def test_remove_movie_from_favorites(client, db_session, test_user):
    movie = Movie(title="Inception", genre="Action", rating=8.8, release_year=2010)
    db_session.add(movie)
    db_session.commit()

    client.post(f"/favorites/{movie.id}", headers={"Authorization": f"Bearer {test_user.token}"})
    response = client.delete(f"/favorites/{movie.id}", headers={"Authorization": f"Bearer {test_user.token}"})
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Movie removed from favorites"
