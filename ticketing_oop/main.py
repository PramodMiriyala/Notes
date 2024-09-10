"""__summary__"""
from ticketing.movie import User, Movie
from ticketing.ticketing import Theater, Screen,Seat
from ticketing.bookings import Screening,Payment,Booking

# create user
user_1 = User(name = 'ram')
user_2 = User(name = 'sam')

# create theater
gokul = Theater(name="Gokul")

#create screen
single_screen = Screen(name = '1')
for index in range(ord('a'),ord('i')):
    for i in range(1,11):
        seat = Seat(chr(index),i)
        single_screen.add_seat(seat)

# adding theater,screens
gokul.add_screens(single_screen)

# adding movie
iron_man = Movie(title="Ironman", language="English")

#screening
screening = Screening(theater=gokul, movie=iron_man)
screening.add_showtime(screen_index=1, show_time="11.30 am")
screening.add_showtime(screen_index=1, show_time="2:00 pm")
screening.add_showtime(screen_index=1, show_time='6:00 pm')
screening.add_showtime(screen_index=1, show_time='9:00 pm')

#payment
p = Payment()
p.payment_done(user_1, 200)
booking = Booking(user_1,gokul,screening,gokul.screens[0].seat[0],p)