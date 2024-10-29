# Task 1.1
class Movie:
    def __init__(self, title, duration, rating, screening_timings, max_seats=50):
        self.title = title
        self.duration = duration
        self.rating = rating
        self.screening_timings = screening_timings
        self.max_seats = max_seats
        self.price = 10

class IMAX(Movie):
    def __init__(self, title, duration, rating, screening_timings):
        super().__init__(title, duration, rating, screening_timings, max_seats=30)
        self.price = 15

# Create movie instances
venom = IMAX('Venom', 112, 6.6, ['11:00 AM', '2:00 PM', '5:00 PM', '8:00 PM', '11:00 PM'])
dark_knight = Movie('The Dark Knight', 152, 9.0, ['8:00 AM', '12:00 PM', '4:00 PM', '8:00 PM'])


#Task 1.2

class Movie:
    def __init__(self, title, duration, rating, screening_timings, max_seats=50):
        self.title = title
        self.duration = duration
        self.rating = rating
        self.screening_timings = screening_timings
        self.max_seats = max_seats
        self.price = 10
        self.seats_available = {time: max_seats for time in screening_timings}  # addition of seats_available attribute

    def reduce_seating(self, time, number_of_seats):
            if time in self.seats_available:
                if self.seats_available[time] >= number_of_seats:  # checks if available seats is greater than number of seats to be reduced
                    self.seats_available[time] -= number_of_seats
                    return f"{number_of_seats} seats successfully booked for {self.title} at {time}. Seats remaining: {self.seats_available[time]}"
                else:
                    return f"Not enough seats available for {self.title} at {time}. Available: {self.seats_available[time]}"
            else:
                return "Invalid screening time."

    def display_info(self):
        print(f"Title: {self.title}\nDuration: {self.duration} minutes\nRating: {self.rating}/10\nPrice: ${self.price}\n")
        for time, seats in self.seats_available:
            print(f"{time}: {seats}")

# Test
print(dark_knight.seats_available['8:00 AM'])
dark_knight.reduce_seating('8:00 AM', 3)
print(dark_knight.seats_available['8:00 AM'])


# Task 1.3

class Booking:
    def __init__(self, user_name, movie, number_of_seats):
        self.user_name = user_name
        self.movie = movie
        self.number_of_seats = number_of_seats

    def confirm_booking(self, time):
        if self.number_of_seats < 1:
            return False, "You must book at least one seat."
        if self.number_of_seats > self.movie.seats_available[time]:
            return False, "Not enough seats available for the selected time."
        else:
            self.movie.reduce_seating(time, self.number_of_seats)  #removes seats from available seats
            return True, "Booking confirmed!"

    def cal_price(self):
        return self.number_of_seats * self.movie.price

# Test cases:
booking1 = Booking('Alice', dark_knight, 3)  # normal case
booking1.confirm_booking('8:00 AM')

booking2 = Booking('Bob', dark_knight, 0)  # erroneous case
booking2.confirm_booking('8:00 AM')

booking3 = Booking('Charlie', dark_knight, 50)  # erroneous case
booking3.confirm_booking('8:00 AM')

booking4 = Booking('Diana', venom, 50)  # boundary case
booking4.confirm_booking('11:00 AM')


# Task 1.4

def movie_booking_system():
    # Display movie information
    venom.display_info()
    dark_knight.display_info()

    # Prompt user for booking details
    user_name = input("Enter your name: ")
    movie_title = input("Enter movie title (Venom or The Dark Knight): ")

    # Select movie based on user input
    if movie_title.lower() == "venom":
        selected_movie = venom
    elif movie_title.lower() == "the dark knight":
        selected_movie = dark_knight
    else:
        return "Movie not found."

    screening_time = input("Enter screening time: ")
    number_of_seats = int(input("Enter number of seats requested: "))

    # Create booking
    booking5 = Booking(user_name, selected_movie, number_of_seats)
    is_confirmed, message = booking5.confirm_booking(screening_time)

    if is_confirmed:
        # Update movie information
        total_price = booking5.cal_price()
        print(f"Booking successful! Total price: ${total_price}")
    else:
        print(message)

# Calls the movie booking system function
movie_booking_system()