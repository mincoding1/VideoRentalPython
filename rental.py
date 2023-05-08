from movie import Movie

class Rental:
    def __init__(self, movie: Movie, daysRented: int):
        self.__days_rented = daysRented
        self.__movie = movie

    def get_charge(self):
        this_amount = 0.0
        if self.get_movie().get_price_code() == Movie.REGULAR:
            this_amount += 2
            if self.get_days_rented() > 2:
                this_amount += (self.get_days_rented() - 2) * 1.5
        elif self.get_movie().get_price_code() == Movie.NEW_RELEASE:
            this_amount += self.get_days_rented() * 3
        elif self.get_movie().get_price_code() == Movie.CHILDRENS:
            this_amount += 1.5
            if self.get_days_rented() > 3:
                this_amount += (self.get_days_rented() - 3) * 1.5
        return this_amount

    def get_days_rented(self):
        return self.__days_rented

    def get_movie(self):
        return self.__movie


