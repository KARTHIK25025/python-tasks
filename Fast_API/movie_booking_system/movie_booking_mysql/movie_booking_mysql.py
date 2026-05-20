# ============================================================
# 🎬 FastAPI Movie Ticket Booking System
# ✅ SQLAlchemy Version
# pip install fastapi uvicorn sqlalchemy pymysql
# ============================================================

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

# ------------------------------------------------------------
# 🚀 App Configuration
# ------------------------------------------------------------

app = FastAPI()

# ------------------------------------------------------------
# 🗄️ DATABASE CONFIGURATION
# ------------------------------------------------------------

# SQLite
DATABASE_URL = "sqlite:///./movie_booking.db"

# MySQL Example
# DATABASE_URL = "mysql+pymysql://root:root@localhost/movie_booking"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
Base = declarative_base()

# ------------------------------------------------------------
# 🧱 DATABASE TABLES
# ------------------------------------------------------------

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    theater = Column(String)
    show_time = Column(String)
    available_seats = Column(Integer)


class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer)
    movie_name = Column(String)
    user_name = Column(String)
    status = Column(String)


# Create Tables
Base.metadata.create_all(bind=engine)

# ------------------------------------------------------------
# 📦 Pydantic Schemas
# ------------------------------------------------------------

class MovieSchema(BaseModel):
    name: str
    theater: str
    show_time: str
    available_seats: int
class BookingSchema(BaseModel):
    user_name: str


# ------------------------------------------------------------
# 🔄 DATABASE DEPENDENCY
# ------------------------------------------------------------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------------------------------------------------
# 🏠 HOME
# ------------------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "Movie Ticket Booking System Running"
    }

# ------------------------------------------------------------
# ✅ CREATE MOVIE
# ------------------------------------------------------------

@app.post("/movies")
def create_movie(
    movie: MovieSchema,
    db: Session = Depends(get_db)
):
    new_movie = Movie(
        name=movie.name,
        theater=movie.theater,
        show_time=movie.show_time,
        available_seats=movie.available_seats
    )
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return {
        "message": "Movie Added Successfully",
        "data": new_movie
    }

# ------------------------------------------------------------
# ✅ GET ALL MOVIES
# ------------------------------------------------------------

@app.get("/movies")
def get_movies(db: Session = Depends(get_db)):
    movies = db.query(Movie).all()
    return {
        "count": len(movies),
        "data": movies
    }

# ------------------------------------------------------------
# ✅ GET MOVIE BY ID
# ------------------------------------------------------------

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(
        Movie.id == movie_id
    ).first()
    if not movie:
        raise HTTPException(
            status_code=404,
            detail="Movie Not Found"
        )
    return movie

# ------------------------------------------------------------
# ✅ UPDATE MOVIE
# ------------------------------------------------------------

@app.put("/movies/{movie_id}")
def update_movie(
    movie_id: int,
    updated_movie: MovieSchema,
    db: Session = Depends(get_db)
):
    movie = db.query(Movie).filter(
        Movie.id == movie_id
    ).first()
    if not movie:
        raise HTTPException(
            status_code=404,
            detail="Movie Not Found"
        )
    movie.name = updated_movie.name
    movie.theater = updated_movie.theater
    movie.show_time = updated_movie.show_time
    movie.available_seats = updated_movie.available_seats
    db.commit()
    db.refresh(movie)
    return {
        "message": "Movie Updated Successfully",
        "data": movie
    }

# ------------------------------------------------------------
# ✅ DELETE MOVIE
# ------------------------------------------------------------

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(
        Movie.id == movie_id
    ).first()
    if not movie:
        raise HTTPException(
            status_code=404,
            detail="Movie Not Found"
        )
    db.delete(movie)
    db.commit()
    return {
        "message": "Movie Deleted Successfully"
    }

# ------------------------------------------------------------
# 🎟️ BOOK TICKET
# ------------------------------------------------------------

@app.post("/book-ticket/{movie_id}")
def book_ticket(
    movie_id: int,
    booking: BookingSchema,
    db: Session = Depends(get_db)
):
    movie = db.query(Movie).filter(
        Movie.id == movie_id
    ).first()
    if not movie:
        raise HTTPException(
            status_code=404,
            detail="Movie Not Found"
        )
    if movie.available_seats <= 0:
        raise HTTPException(
            status_code=400,
            detail="No Seats Available"
        )
    movie.available_seats -= 1
    new_booking = Booking(
        movie_id=movie.id,
        movie_name=movie.name,
        user_name=booking.user_name,
        status="Booked"
    )
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return {
        "message": "Ticket Booked Successfully",
        "data": new_booking
    }

# ------------------------------------------------------------
# ❌ CANCEL TICKET
# ------------------------------------------------------------

@app.post("/cancel-ticket/{booking_id}")
def cancel_ticket(
    booking_id: int,
    db: Session = Depends(get_db)
):
    booking = db.query(Booking).filter(
        Booking.id == booking_id
    ).first()
    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking Not Found"
        )
    if booking.status == "Cancelled":
        raise HTTPException(
            status_code=400,
            detail="Already Cancelled"
        )
    booking.status = "Cancelled"
    movie = db.query(Movie).filter(
        Movie.id == booking.movie_id
    ).first()
    if movie:
        movie.available_seats += 1
    db.commit()
    return {
        "message": "Ticket Cancelled Successfully",
        "data": booking
    }

# ------------------------------------------------------------
# 🎬 AVAILABLE SHOWS
# ------------------------------------------------------------

@app.get("/available-shows")
def available_shows(db: Session = Depends(get_db)):
    movies = db.query(Movie).filter(
        Movie.available_seats > 0
    ).all()
    return movies

# ------------------------------------------------------------
# 📋 ALL BOOKINGS
# ------------------------------------------------------------

@app.get("/bookings")
def get_bookings(db: Session = Depends(get_db)):
    bookings = db.query(Booking).all()
    return bookings

# ------------------------------------------------------------
# 🔍 SEARCH MOVIE
# ------------------------------------------------------------

@app.get("/search-movie/{name}")
def search_movie(name: str, db: Session = Depends(get_db)):
    movies = db.query(Movie).filter(
        Movie.name.ilike(f"%{name}%")
    ).all()
    if not movies:
        raise HTTPException(
            status_code=404,
            detail="Movie Not Found"
        )
    return movies