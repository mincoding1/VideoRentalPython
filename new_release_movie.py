from movie import Movie

class NewReleaseMovie(Movie):
    def __init__(self, title: str):
        super().__init__(title, Movie.NEW_RELEASE)

    def get_charge_for(self, days_rented):
        this_amount = 0.0
        this_amount += days_rented * 3
        return this_amount

    def get_frequent_renter_points_for(self, days_rented):
        if days_rented > 1:
            return 2
        return 1

