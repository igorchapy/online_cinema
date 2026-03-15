from sqlalchemy import select
from models import Movie
from fastapi import HTTPException


async def get_movie_by_uuid(db, uuid):

    query = select(Movie).where(Movie.uuid == uuid)

    result = await db.execute(query)

    movie = result.scalar_one_or_none()

    if not movie:
        raise HTTPException(404, "Movie not found")

    return movie
