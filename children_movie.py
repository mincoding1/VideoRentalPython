from movie import Movie

class ChildrenMovie(Movie):
    def __init__(self, title: str):
        super().__init__(title, Movie.CHILDRENS)

    def get_charge_for(self, days_rented):
        this_amount = 1.5
        if days_rented > 3:
            this_amount += (days_rented - 3) * 1.5
        return this_amount

    def get_frequent_renter_points_for(self, days_rented):
        return 1

