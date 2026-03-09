import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, SessionLocal
from app.models import Movie


@pytest.fixture(scope="module")
def client():
    Base.metadata.create_all(bind=engine)
    yield TestClient(app)
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def db_session():
    session = SessionLocal()
    session.query(Movie).delete()
    session.commit()
    yield session
    session.close()

def test_list_movies_success(client, db_session):
    movie1 = Movie(title="Inception", genre="Action", rating=8.8, release_year=2010)
    movie2 = Movie(title="Interstellar", genre="Sci-Fi", rating=8.6, release_year=2014)
    db_session.add_all([movie1, movie2])
    db_session.commit()

    response = client.get("/movies")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 2
    assert len(data["movies"]) == 2

def test_list_movies_with_genre_filter(client, db_session):
    movie = Movie(title="The Dark Knight", genre="Action", rating=9.0, release_year=2008)
    db_session.add(movie)
    db_session.commit()

    response = client.get("/movies?genre=Action")
    assert response.status_code == 200
    data = response.json()
    assert all(m["genre"] == "Action" for m in data["movies"])

def test_list_movies_with_rating_filter(client, db_session):
    movie1 = Movie(title="Movie A", genre="Drama", rating=7.0, release_year=2015)
    movie2 = Movie(title="Movie B", genre="Drama", rating=8.5, release_year=2016)
    db_session.add_all([movie1, movie2])
    db_session.commit()

    response = client.get("/movies?min_rating=8")
    assert response.status_code == 200
    data = response.json()
    assert all(m["rating"] >= 8 for m in data["movies"])

def test_list_movies_pagination(client, db_session):
    movies = [Movie(title=f"Movie {i}", genre="Comedy", rating=5 + i, release_year=2000 + i) for i in range(5)]
    db_session.add_all(movies)
    db_session.commit()

    response = client.get("/movies?page=2&limit=2")
    assert response.status_code == 200
    data = response.json()
    assert data["page"] == 2
    assert data["limit"] == 2
    assert len(data["movies"]) == 2
