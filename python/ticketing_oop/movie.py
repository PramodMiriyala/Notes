"""dummy ticketing code"""
class Movie:
    """movie class"""
    def __init__(self, title, language):
        """_summary_"""
        self._title = title
        self._language = language

    @property
    def title(self):
        """_summary_"""
        return self._title
    @title.setter
    def title(self, value):
        self._title = value
    @property
    def language(self):
        """_summary_"""
        return self._language
    @language.setter
    def language(self, value):
        self._language = value

    def __str__(self):
        return f"{self._title} : {self._language}"

class User:
    """user details"""
    def __init__(self, name):
        self.name = name
