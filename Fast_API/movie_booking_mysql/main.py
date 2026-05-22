# ============================================================
# 🎬 FastAPI Movie Ticket Booking System - Ultimate Edition
# Database: MySQL | ORM: SQLModel
# ============================================================
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select, func
from typing import List

# ============================================================
# 🚀 APP & DATABASE CONFIGURATION
# ============================================================
app = FastAPI(title="Movie Ticket Booking System")

# MySQL Connection String (Ensure your MySQL server is running and database exists)
DATABASE_URL = "mysql+pymysql://root:Root@localhost:3306/movie_booking_mysql"

engine = create_engine(DATABASE_URL)

# ============================================================
# 🧱 DATABASE MODELS (SQLModel)
# ============================================================
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    email: str

class Movie(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    theater: str
    show_time: str
    available_seats: int
    # NEW FIELDS for Revenue and Top Rated logic
    price: float 
    rating: float = Field(default=0.0)

class Booking(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    movie_id: int = Field(foreign_key="movie.id")
    movie_name: str
    seats_booked: int
    # NEW FIELD for Revenue calculation
    total_price: float 
    status: str = Field(default="Booked") # 'Booked' or 'Cancelled'

# Create tables in MySQL on startup
SQLModel.metadata.create_all(engine)

# ============================================================
# 🔄 DATABASE SESSION DEPENDENCY
# ============================================================
def get_db():
    with Session(engine) as session:
        yield session

@app.get("/")
def home():
    return {"message": "Movie Ticket Booking System Running 🚀"}

# ============================================================
# 🧑‍🤝‍🧑 HELPER ENDPOINT (Create User for Testing)
# ============================================================
@app.post("/users")
def create_user(user: User, db: Session = Depends(get_db)):
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User created", "user": user}


# ============================================================
# 1. ADD MOVIE
# ============================================================
@app.post("/movies")
def add_movie(movie: Movie, db: Session = Depends(get_db)):
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return {"message": "Movie Added Successfully", "data": movie}

# ============================================================
# 2. GET ALL MOVIES
# ============================================================
@app.get("/movies")
def get_all_movies(db: Session = Depends(get_db)):
    movies = db.exec(select(Movie)).all()
    return {"count": len(movies), "data": movies}

# ============================================================
# 3. GET MOVIE BY ID
# ============================================================
@app.get("/movies/{movie_id}")
def get_movie_by_id(movie_id: int, db: Session = Depends(get_db)):
    movie = db.get(Movie, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

# ============================================================
# 4. UPDATE MOVIE
# ============================================================
@app.put("/movies/{movie_id}")
def update_movie(movie_id: int, updated: Movie, db: Session = Depends(get_db)):
    movie = db.get(Movie, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    
    movie.name = updated.name
    movie.theater = updated.theater
    movie.show_time = updated.show_time
    movie.available_seats = updated.available_seats
    movie.price = updated.price
    movie.rating = updated.rating
    
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return {"message": "Movie Updated", "data": movie}

# ============================================================
# 5. DELETE MOVIE
# ============================================================
@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.get(Movie, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    
    db.delete(movie)
    db.commit()
    return {"message": "Movie Deleted Successfully"}

# ============================================================
# 6. BOOK MOVIE TICKET
# ============================================================
@app.post("/book-ticket/{movie_id}")
def book_ticket(movie_id: int, user_id: int, seats_to_book: int = 1, db: Session = Depends(get_db)):
    movie = db.get(Movie, movie_id)
    user = db.get(User, user_id)
    
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if movie.available_seats < seats_to_book:
        raise HTTPException(status_code=400, detail="Not enough seats available")
    
    # Deduct seats
    movie.available_seats -= seats_to_book
    
    # Calculate price and create booking
    total_cost = movie.price * seats_to_book
    new_booking = Booking(
        user_id=user.id,
        movie_id=movie.id,
        movie_name=movie.name,
        seats_booked=seats_to_book,
        total_price=total_cost,
        status="Booked"
    )
    
    db.add(movie)
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return {"message": "Ticket Booked Successfully", "data": new_booking}

# ============================================================
# 7. CANCEL TICKET
# ============================================================
@app.post("/cancel-ticket/{booking_id}")
def cancel_ticket(booking_id: int, db: Session = Depends(get_db)):
    booking = db.get(Booking, booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
        
    if booking.status == "Cancelled":
        raise HTTPException(status_code=400, detail="Ticket is already cancelled")
        
    # Mark as cancelled
    booking.status = "Cancelled"
    
    # Restore seats
    movie = db.get(Movie, booking.movie_id)
    if movie:
        movie.available_seats += booking.seats_booked
        db.add(movie)
        
    db.add(booking)
    db.commit()
    return {"message": "Ticket Cancelled and Seats Restored", "data": booking}

# ============================================================
# 8. GET AVAILABLE SHOWS
# ============================================================
@app.get("/available-shows")
def get_available_shows(db: Session = Depends(get_db)):
    movies = db.exec(select(Movie).where(Movie.available_seats > 0)).all()
    return {"count": len(movies), "data": movies}

# ============================================================
# 9. GET ALL BOOKINGS
# ============================================================
@app.get("/bookings")
def get_all_bookings(db: Session = Depends(get_db)):
    bookings = db.exec(select(Booking)).all()
    return {"count": len(bookings), "data": bookings}

# ============================================================
# 10. SEARCH MOVIE BY NAME
# ============================================================
@app.get("/search-movie/{name}")
def search_movie_by_name(name: str, db: Session = Depends(get_db)):
    movies = db.exec(select(Movie).where(Movie.name.icontains(name))).all()
    if not movies:
        raise HTTPException(status_code=404, detail="No movies found matching that name")
    return movies

# ============================================================
# 11. TOP RATED MOVIES
# ============================================================
@app.get("/top-rated-movies")
def get_top_rated_movies(limit: int = 5, db: Session = Depends(get_db)):
    # Order by rating descending and limit the results
    movies = db.exec(select(Movie).order_by(Movie.rating.desc()).limit(limit)).all()
    return {"data": movies}

# ============================================================
# 12. REMAINING SEATS
# ============================================================
@app.get("/remaining-seats/{movie_id}")
def get_remaining_seats(movie_id: int, db: Session = Depends(get_db)):
    movie = db.get(Movie, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    
    return {
        "movie_name": movie.name,
        "total_remaining_seats": movie.available_seats
    }

# ============================================================
# 13. BOOKING HISTORY (By User)
# ============================================================
@app.get("/booking-history/{user_id}")
def get_booking_history(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        
    history = db.exec(select(Booking).where(Booking.user_id == user_id)).all()
    return {"user": user.username, "total_bookings": len(history), "data": history}

# ============================================================
# 14. TOTAL REVENUE
# ============================================================
@app.get("/total-revenue")
def get_total_revenue(db: Session = Depends(get_db)):
    # Sum the total_price of all bookings that are NOT cancelled
    revenue = db.exec(
        select(func.sum(Booking.total_price)).where(Booking.status == "Booked")
    ).first()
    
    return {"total_revenue": revenue or 0.0}