from rental import Rental
from movie import Movie

class Customer:
    def __init__(self, name: str):
        self.__rentals = []
        self.__name = name

    def get_name(self):
        return self.__name

    def statement(self):
        result = "Rental Record for " + self.get_name() + "\n"

        for each in self.__rentals:
            # show figures for this rental
            result += "\t" + each.get_movie().get_title() + "\t" + str(each.get_charge()) + "\n"

        # add footer lines
        result += "Amount owed is " + str(self.get_total_amount()) + "\n"
        result += "You earned " + str(self.get_frequent_renter_points()) + " frequent renter points"

        return result

    def get_frequent_renter_points(self):
        frequent_renter_points = 0
        for each in self.__rentals:
            frequent_renter_points += each.get_frequent_renter_points_for()
        return frequent_renter_points

    def get_total_amount(self):
        total_amount = 0
        for each in self.__rentals:
            total_amount += each.get_charge()
        return total_amount

    def add_rental(self, param: Rental):
        self.__rentals.append(param)

