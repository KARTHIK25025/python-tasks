from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

# --- IN-MEMORY DATABASE ---
screens = {
    1: {'id': 1, 'name': 'Screen 1 (IMAX)', 'total_seats': 150},
    2: {'id': 2, 'name': 'Screen 2 (Standard)', 'total_seats': 80}
}

movies = {
    1: {'id': 1, 'name': 'Inception', 'genre': 'Sci-Fi'}
}

shows = {}
bookings = {}

movie_id_counter = 2
show_id_counter = 1
booking_id_counter = 1

# --- API ENDPOINTS ---

@app.route('/movies', methods=['POST'])
def add_movie():
    global movie_id_counter
    data = request.json
    if not data or 'name' not in data:
        return jsonify({'error': 'Movie name is required'}), 400
    
    movie = {
        'id': movie_id_counter,
        'name': data.get('name'),
        'genre': data.get('genre', 'Unknown')
    }
    movies[movie_id_counter] = movie
    movie_id_counter += 1
    return jsonify({'message': 'Movie added successfully', 'movie': movie}), 201

@app.route('/movies', methods=['GET'])
def get_all_movies():
    return jsonify(list(movies.values())), 200

@app.route('/shows', methods=['POST'])
def add_show():
    global show_id_counter
    data = request.json
    
    movie_id = data.get('movie_id')
    screen_id = data.get('screen_id')
    
    if movie_id not in movies or screen_id not in screens:
        return jsonify({'error': 'Invalid Movie ID or Screen ID'}), 400
        
    screen = screens[screen_id]
    
    show = {
        'id': show_id_counter,
        'movie_id': movie_id,
        'screen_id': screen_id,
        'show_date': data.get('show_date'),  
        'show_time': data.get('show_time'),  
        'total_seats': screen['total_seats'],
        'available_seats': screen['total_seats'],
        'booked_seats': [] # Track specific seat numbers here
    }
    shows[show_id_counter] = show
    show_id_counter += 1
    return jsonify({'message': 'Show scheduled successfully', 'show': show}), 201

@app.route('/shows', methods=['GET'])
def get_all_shows():
    enriched_shows = []
    for show in shows.values():
        enriched = show.copy()
        enriched['movie_name'] = movies[show['movie_id']]['name']
        enriched['screen_name'] = screens[show['screen_id']]['name']
        enriched_shows.append(enriched)
    return jsonify(enriched_shows), 200

@app.route('/book-ticket/<int:show_id>', methods=['POST'])
def book_ticket(show_id):
    global booking_id_counter
    show = shows.get(show_id)
    
    if not show:
        return jsonify({'error': 'Show not found'}), 404
    
    data = request.json
    requested_seats = data.get('seat_numbers', []) # Expects a list like [12, 13]
    customer_name = data.get('customer_name', 'Guest')
    
    if not requested_seats:
        return jsonify({'error': 'You must select at least one seat number'}), 400
        
    # Validate each requested seat
    for seat in requested_seats:
        if seat < 1 or seat > show['total_seats']:
            return jsonify({'error': f'Invalid seat number: {seat}. Max seats: {show["total_seats"]}'}), 400
        if seat in show['booked_seats']:
            return jsonify({'error': f'Seat {seat} is already booked!'}), 400
            
    # Mark seats as booked
    show['booked_seats'].extend(requested_seats)
    show['available_seats'] -= len(requested_seats)
    
    booking_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    booking = {
        'booking_id': booking_id_counter,     # Clearly labeled Booking ID
        'movie_id': show['movie_id'],         # Tied directly to the Movie ID
        'movie_name': movies[show['movie_id']]['name'],
        'show_id': show_id,
        'customer_name': customer_name,
        'seat_numbers': requested_seats,      # Track exact seats
        'total_tickets': len(requested_seats),
        'booking_date': booking_timestamp,
        'show_date': show['show_date'],
        'show_time': show['show_time']
    }
    bookings[booking_id_counter] = booking
    booking_id_counter += 1
    
    return jsonify({'message': 'Ticket(s) booked successfully', 'booking': booking}), 201

@app.route('/cancel-ticket/<int:booking_id>', methods=['POST'])
def cancel_ticket(booking_id):
    booking = bookings.get(booking_id)
    if not booking:
        return jsonify({'error': 'Booking not found'}), 404
        
    show_id = booking['show_id']
    show = shows.get(show_id)
    
    if show:
        # Free up the specific seats that were cancelled
        for seat in booking['seat_numbers']:
            if seat in show['booked_seats']:
                show['booked_seats'].remove(seat)
        show['available_seats'] += booking['total_tickets']
        
    del bookings[booking_id]
    return jsonify({'message': f'Booking ID {booking_id} cancelled successfully'}), 200

@app.route('/bookings', methods=['GET'])
def get_bookings():
    return jsonify(list(bookings.values())), 200

# --- ROUTES ---
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)