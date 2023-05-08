from abc import ABC, abstractmethod

class Movie(ABC):
    CHILDRENS = 2
    NEW_RELEASE = 1
    REGULAR = 0

    def __init__(self, title: str, price_code):
        self.__title = title
        self.__price_code = price_code

    @abstractmethod
    def get_charge_for(self, days_rented):
        pass

    @abstractmethod
    def get_frequent_renter_points_for(self, days_rented):
        pass

    def get_price_code(self):
        return self.__price_code

    def set_price_code(self, arg):
        self.__price_code = arg

    def get_title(self):
        return self.__title


