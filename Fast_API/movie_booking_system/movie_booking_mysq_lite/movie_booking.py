# ============================================================
# 🎬 FastAPI Movie Ticket Booking System
# ✅ SQLite Version
# pip install fastapi uvicorn sqlalchemy
# ============================================================

from fastapi import FastAPI, HTTPException
import sqlite3

# ------------------------------------------------------------
# 🚀 FastAPI App
# ------------------------------------------------------------

app = FastAPI()

# ------------------------------------------------------------
# 🗄️ SQLite Database Connection
# ------------------------------------------------------------

conn = sqlite3.connect(
    "movie_booking.db",
    check_same_thread=False
)

cursor = conn.cursor()

# ------------------------------------------------------------
# 🧱 Create Tables
# ------------------------------------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY,
    name TEXT,
    genre TEXT,
    theater TEXT,
    show_time TEXT,
    total_seats INTEGER,
    available_seats INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS bookings(
    booking_id INTEGER PRIMARY KEY,
    movie_id INTEGER,
    movie_name TEXT,
    user_name TEXT,
    tickets INTEGER,
    status TEXT
)
""")

conn.commit()

# ------------------------------------------------------------
# 🏠 Home API
# ------------------------------------------------------------

@app.get("/")
def home():

    return {
        "message": "Movie Ticket Booking System Using SQLite"
    }


# ------------------------------------------------------------
# ✅ Add Movie
# ------------------------------------------------------------

@app.post("/movies")
def add_movie(movie: dict):

    query = """
    INSERT INTO movies
    VALUES(?,?,?,?,?,?,?)
    """

    values = (
        movie["id"],
        movie["name"],
        movie["genre"],
        movie["theater"],
        movie["show_time"],
        movie["total_seats"],
        movie["available_seats"]
    )

    cursor.execute(query, values)

    conn.commit()

    return {
        "message": "Movie Added Successfully"
    }


# ------------------------------------------------------------
# ✅ Get All Movies
# ------------------------------------------------------------

@app.get("/movies")
def get_movies():

    query = "SELECT * FROM movies"

    cursor.execute(query)

    data = cursor.fetchall()

    return data


# ------------------------------------------------------------
# ✅ Get Movie By ID
# ------------------------------------------------------------

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):

    query = "SELECT * FROM movies WHERE id=?"

    cursor.execute(query, (movie_id,))

    movie = cursor.fetchone()

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

    query = """
    UPDATE movies
    SET name=?,
        genre=?,
        theater=?,
        show_time=?,
        total_seats=?,
        available_seats=?
    WHERE id=?
    """

    values = (
        updated_movie["name"],
        updated_movie["genre"],
        updated_movie["theater"],
        updated_movie["show_time"],
        updated_movie["total_seats"],
        updated_movie["available_seats"],
        movie_id
    )

    cursor.execute(query, values)

    conn.commit()

    return {
        "message": "Movie Updated Successfully"
    }


# ------------------------------------------------------------
# ✅ Delete Movie
# ------------------------------------------------------------

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):

    query = "DELETE FROM movies WHERE id=?"

    cursor.execute(query, (movie_id,))

    conn.commit()

    return {
        "message": "Movie Deleted Successfully"
    }


# ------------------------------------------------------------
# 🎟️ Book Ticket
# ------------------------------------------------------------

@app.post("/book-ticket/{movie_id}")
def book_ticket(movie_id: int,
                booking: dict):

    # Get Movie

    query = "SELECT * FROM movies WHERE id=?"

    cursor.execute(query, (movie_id,))

    movie = cursor.fetchone()

    if not movie:
        raise HTTPException(
            status_code=404,
            detail="Movie Not Found"
        )

    available_seats = movie[6]

    if available_seats < booking["tickets"]:
        raise HTTPException(
            status_code=400,
            detail="Not Enough Seats"
        )

    # Reduce Seats

    remaining = available_seats - booking["tickets"]

    update_query = """
    UPDATE movies
    SET available_seats=?
    WHERE id=?
    """

    cursor.execute(
        update_query,
        (remaining, movie_id)
    )

    # Insert Booking

    insert_query = """
    INSERT INTO bookings
    VALUES(?,?,?,?,?,?)
    """

    values = (
        booking["booking_id"],
        movie_id,
        movie[1],
        booking["user_name"],
        booking["tickets"],
        "Booked"
    )

    cursor.execute(insert_query, values)

    conn.commit()

    return {
        "message": "Ticket Booked Successfully",
        "remaining_seats": remaining
    }


# ------------------------------------------------------------
# ❌ Cancel Ticket
# ------------------------------------------------------------

@app.post("/cancel-ticket/{booking_id}")
def cancel_ticket(booking_id: int):

    # Get Booking

    query = """
    SELECT * FROM bookings
    WHERE booking_id=?
    """

    cursor.execute(query, (booking_id,))

    booking = cursor.fetchone()

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking Not Found"
        )

    if booking[5] == "Cancelled":
        raise HTTPException(
            status_code=400,
            detail="Already Cancelled"
        )

    movie_id = booking[1]

    # Get Movie

    movie_query = """
    SELECT * FROM movies
    WHERE id=?
    """

    cursor.execute(movie_query, (movie_id,))

    movie = cursor.fetchone()

    new_seats = movie[6] + booking[4]

    # Update Seats

    update_movie = """
    UPDATE movies
    SET available_seats=?
    WHERE id=?
    """

    cursor.execute(
        update_movie,
        (new_seats, movie_id)
    )

    # Update Booking Status

    update_booking = """
    UPDATE bookings
    SET status=?
    WHERE booking_id=?
    """

    cursor.execute(
        update_booking,
        ("Cancelled", booking_id)
    )

    conn.commit()

    return {
        "message": "Ticket Cancelled Successfully"
    }


# ------------------------------------------------------------
# 🎬 Available Shows
# ------------------------------------------------------------

@app.get("/available-shows")
def available_shows():

    query = """
    SELECT * FROM movies
    WHERE available_seats > 0
    """

    cursor.execute(query)

    data = cursor.fetchall()

    return data


# ------------------------------------------------------------
# 📋 Get All Bookings
# ------------------------------------------------------------

@app.get("/bookings")
def get_bookings():

    query = "SELECT * FROM bookings"

    cursor.execute(query)

    data = cursor.fetchall()

    return data


# ------------------------------------------------------------
# 🔍 Search Movie
# ------------------------------------------------------------

@app.get("/search-movie/{name}")
def search_movie(name: str):

    query = """
    SELECT * FROM movies
    WHERE name LIKE ?
    """

    value = ("%" + name + "%",)

    cursor.execute(query, value)

    movies = cursor.fetchall()

    if not movies:
        raise HTTPException(
            status_code=404,
            detail="Movie Not Found"
        )

    return movies