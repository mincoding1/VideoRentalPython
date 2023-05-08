class Movie:
    CHILDRENS = 2
    NEW_RELEASE = 1
    REGULAR = 0

    def __init__(self, title: str, price_code):
        self.__title = title
        self.__price_code = price_code

    def get_charge_for(self, days_rented):
        this_amount = 0.0
        if self.get_price_code() == Movie.REGULAR:
            this_amount += 2
            if days_rented > 2:
                this_amount += (days_rented - 2) * 1.5
        elif self.get_price_code() == Movie.NEW_RELEASE:
            this_amount += days_rented * 3
        elif self.get_price_code() == Movie.CHILDRENS:
            this_amount += 1.5
            if days_rented > 3:
                this_amount += (days_rented - 3) * 1.5
        return this_amount

    def get_frequent_renter_points_for(self, days_rented):
        # add bonus for a two day new release rental
        if (self.get_price_code() == Movie.NEW_RELEASE) and days_rented > 1:
            return 2
        return 1

    def get_price_code(self):
        return self.__price_code

    def set_price_code(self, arg):
        self.__price_code = arg

    def get_title(self):
        return self.__title


