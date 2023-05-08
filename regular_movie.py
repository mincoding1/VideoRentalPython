from movie import Movie

class RegularMovie(Movie):
    def __init__(self, title: str):
        super().__init__(title, Movie.REGULAR)

    def get_charge_for(self, days_rented):
        this_amount = 2.0
        if days_rented > 2:
            this_amount += (days_rented - 2) * 1.5
        return this_amount

    def get_frequent_renter_points_for(self, days_rented):
        return 1

