from pydantic import BaseModel


class MovieBase(BaseModel):
    name: str
    year: int
    imdb: float


class MovieCreate(MovieBase):
    description: str


class MovieResponse(MovieBase):
    id: int

    class Config:
        from_attributes = True
