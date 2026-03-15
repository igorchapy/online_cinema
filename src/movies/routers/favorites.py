from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db
from models.movie import Movie

router = APIRouter(prefix="/favourites", tags=["favorites"])


@router.get("/")
async def get_movies(
    page: int = 1,
    limit: int = 20,
    db: AsyncSession = Depends(get_db)
):

    offset = (page - 1) * limit

    query = select(Movie).offset(offset).limit(limit)

    result = await db.execute(query)

    movies = result.scalars().all()

    return movies
