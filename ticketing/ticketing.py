"""teater related st"""
class Seat:
    """__summary__"""
    def __init__(self, row, number):
        self._row = row
        self._number = number
    @property
    def row(self):
        """__summart__"""
        return self._row
    def number(self):
        """__summary__"""
        return self._number

class Screen:
    """__summary__"""
    def __init__(self, name):
        self.name = name
        self.seats = []
    def add_seat(self, seat):
        """__summary__"""
        self.seats.append(seat)

class Theater:
    """__summary__"""
    def __init__(self, name):
        self.name = name
        self.screens = []
    def add_screens(self, screen):
        """__summary__"""
        self.screens.append(screen)
