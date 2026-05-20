# ============================================================
# 🎬 FastAPI Movie Ticket Booking System
# ✅ MongoDB Version
# pip install fastapi uvicorn pymongo
# ============================================================

from fastapi import FastAPI, HTTPException
from pymongo import MongoClient

# ------------------------------------------------------------
# 🚀 FastAPI App
# ------------------------------------------------------------

app = FastAPI()

# ------------------------------------------------------------
# 🍃 MongoDB Connection
# ------------------------------------------------------------

client = MongoClient("mongodb://localhost:27017")

db = client["movie_booking_db"]

movie_collection = db["movies"]

booking_collection = db["bookings"]

# ------------------------------------------------------------
# 🏠 Home API
# ------------------------------------------------------------

@app.get("/")
def home():

    return {
        "message": "Movie Ticket Booking System Using MongoDB"
    }


# ------------------------------------------------------------
# ✅ Add Movie
# ------------------------------------------------------------

@app.post("/movies")
def add_movie(movie: dict):

    existing_movie = movie_collection.find_one(
        {"id": movie["id"]}
    )

    if existing_movie:
        raise HTTPException(
            status_code=400,
            detail="Movie ID Already Exists"
        )

    movie_collection.insert_one(movie)

    return {
        "message": "Movie Added Successfully",
        "data": movie
    }


# ------------------------------------------------------------
# ✅ Get All Movies
# ------------------------------------------------------------

@app.get("/movies")
def get_movies():

    movies = list(movie_collection.find({}, {"_id": 0}))

    return movies


# ------------------------------------------------------------
# ✅ Get Movie By ID
# ------------------------------------------------------------

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):

    movie = movie_collection.find_one(
        {"id": movie_id},
        {"_id": 0}
    )

    if not movie:
        raise HTTPException(
            status_code=404,
            detail="Movie Not Found"
        )

    return movie


# ------------------------------------------------------------
# ✅ Update Movie
# ------------------------------------------------------------

@app.put("/movies/{movie_id}")
def update_movie(movie_id: int,
                 updated_movie: dict):

    movie = movie_collection.find_one(
        {"id": movie_id}
    )

    if not movie:
        raise HTTPException(
            status_code=404,
            detail="Movie Not Found"
        )

    movie_collection.update_one(
        {"id": movie_id},
        {
            "$set": updated_movie
        }
    )

    return {
        "message": "Movie Updated Successfully"
    }


# ------------------------------------------------------------
# ✅ Delete Movie
# ------------------------------------------------------------

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):

    movie = movie_collection.find_one(
        {"id": movie_id}
    )

    if not movie:
        raise HTTPException(
            status_code=404,
            detail="Movie Not Found"
        )

    movie_collection.delete_one(
        {"id": movie_id}
    )

    return {
        "message": "Movie Deleted Successfully"
    }


# ------------------------------------------------------------
# 🎟️ Book Ticket
# ------------------------------------------------------------

@app.post("/book-ticket/{movie_id}")
def book_ticket(movie_id: int,
                booking: dict):

    movie = movie_collection.find_one(
        {"id": movie_id}
    )

    if not movie:
        raise HTTPException(
            status_code=404,
            detail="Movie Not Found"
        )

    if movie["available_seats"] < booking["tickets"]:
        raise HTTPException(
            status_code=400,
            detail="Not Enough Seats Available"
        )

    # Reduce seats

    remaining_seats = (
        movie["available_seats"] - booking["tickets"]
    )

    movie_collection.update_one(
        {"id": movie_id},
        {
            "$set": {
                "available_seats": remaining_seats
            }
        }
    )

    # Create Booking

    booking_data = {
        "booking_id": booking["booking_id"],
        "movie_id": movie_id,
        "movie_name": movie["name"],
        "user_name": booking["user_name"],
        "tickets": booking["tickets"],
        "status": "Booked"
    }

    booking_collection.insert_one(booking_data)

    return {
        "message": "Ticket Booked Successfully",
        "remaining_seats": remaining_seats,
        "booking": booking_data
    }


# ------------------------------------------------------------
# ❌ Cancel Ticket
# ------------------------------------------------------------

@app.post("/cancel-ticket/{booking_id}")
def cancel_ticket(booking_id: int):

    booking = booking_collection.find_one(
        {"booking_id": booking_id}
    )

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking Not Found"
        )

    if booking["status"] == "Cancelled":
        raise HTTPException(
            status_code=400,
            detail="Ticket Already Cancelled"
        )

    # Increase seats

    movie = movie_collection.find_one(
        {"id": booking["movie_id"]}
    )

    new_seats = (
        movie["available_seats"] + booking["tickets"]
    )

    movie_collection.update_one(
        {"id": booking["movie_id"]},
        {
            "$set": {
                "available_seats": new_seats
            }
        }
    )

    # Update booking status

    booking_collection.update_one(
        {"booking_id": booking_id},
        {
            "$set": {
                "status": "Cancelled"
            }
        }
    )

    return {
        "message": "Ticket Cancelled Successfully"
    }


# ------------------------------------------------------------
# 🎬 Available Shows
# ------------------------------------------------------------

@app.get("/available-shows")
def available_shows():

    movies = list(
        movie_collection.find(
            {"available_seats": {"$gt": 0}},
            {"_id": 0}
        )
    )

    return movies


# ------------------------------------------------------------
# 📋 Get All Bookings
# ------------------------------------------------------------

@app.get("/bookings")
def get_bookings():

    bookings = list(
        booking_collection.find({}, {"_id": 0})
    )

    return bookings


# ------------------------------------------------------------
# 🔍 Search Movie
# ------------------------------------------------------------

@app.get("/search-movie/{name}")
def search_movie(name: str):
    movies = list(
        movie_collection.find(
            {
                "name": {
                    "$regex": name,
                    "$options": "i"
                }
            },
            {"_id": 0}
        )
    )
    if not movies:
        raise HTTPException(
            status_code=404,
            detail="Movie Not Found"
        )
    return movies