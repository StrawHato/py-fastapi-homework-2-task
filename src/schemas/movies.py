from typing import List, Optional

from pydantic import BaseModel
from datetime import date


class CountryBase(BaseModel):
    code: str
    name: str


class CountryCreate(CountryBase):
    pass


class CountryRead(CountryBase):
    id: int

    class Config:
        from_attributes = True


class GALBase(BaseModel):
    name: str


class GALCreate(GALBase):
    pass


class GALRead(GALBase):
    id: int

    class Config:
        from_attributes = True


class MovieBase(BaseModel):
    name: str
    date: date
    score: float
    overview: str
    status: str
    budget: float
    revenue: float


class MovieCreate(MovieBase):
    country: str
    genres: List[str]
    actors: List[str]
    languages: List[str]


class MovieUpdate(MovieBase):
    pass


class MovieDetailRead(MovieBase):
    id: int
    country: CountryRead
    genres: List[GALRead]
    actors: List[GALRead]
    languages: List[GALRead]

    class Config:
        from_attributes = True


class MovieListRead(BaseModel):
    movies: List[MovieDetailRead]
    prev_page: Optional[str] = None
    next_page: Optional[str] = None
    total_pages: int
    total_items: int

    class Config:
        from_attributes = True
