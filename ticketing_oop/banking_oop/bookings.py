"""ticketing classes"""
class Screening:
    """screen class"""
    def __init__(self, theater, movie):
        self.theater = theater
        self.movie = movie
    def add_showtime(self, screen_index, show_time):
        """movie_time"""
        pass

class Booking:
    """__summary__"""
    def book_ticket(self, user, theater, screening, seat, payment):
        pass

class Payment:
    """__summary__"""
    def payment_done(self, user, ammount):
        pass
