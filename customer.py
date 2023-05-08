from rental import Rental
from movie import Movie

class Customer:
    def __init__(self, name: str):
        self.__rentals = []
        self.__name = name

    def get_name(self):
        return self.__name

    def statement(self):
        total_amount = 0
        frequent_renter_points = 0
        result = "Rental Record for " + self.get_name() + "\n"

        for each in self.__rentals:

            # determine amounts for each line
            # add frequent renter points
            frequent_renter_points += 1
            # add bonus for a two day new release rental
            if (each.get_movie().get_price_code() == Movie.NEW_RELEASE) and each.get_days_rented() > 1:
                frequent_renter_points += 1

            # show figures for this rental
            result += "\t" + each.get_movie().get_title() + "\t" + str(each.get_charge()) + "\n"
            total_amount += each.get_charge()

        # add footer lines
        result += "Amount owed is " + str(total_amount) + "\n"
        result += "You earned " + str(frequent_renter_points) + " frequent renter points"

        return result

    def add_rental(self, param: Rental):
        self.__rentals.append(param)

