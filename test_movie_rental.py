from unittest import TestCase
from customer import Customer, Rental, Movie
from regular_movie import RegularMovie
from new_release_movie import NewReleaseMovie
from children_movie import ChildrenMovie

TITLE = 'TITLE_NOT_IMPORTANT'
NAME = 'NAME_NOT_IMPORTANT'

class Tests(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.customer = Customer(NAME)

    def test_return_new_customer(self):
        self.assertIsNotNone(self.customer)

    def test_statement_for_no_rental(self):
        #assert
        self.assertEqual(self.customer.statement(),
                         'Rental Record for NAME_NOT_IMPORTANT\n'
                         + 'Amount owed is 0\n'
                         + 'You earned 0 frequent renter points')

    def test_statement_for_regular_movie_rental_for_less_than_3_days(self):
        #arrange
        self.customer.add_rental(self.create_rental_for(2, Movie.REGULAR))

        #assert
        self.assertEqual(self.customer.statement(),
                         'Rental Record for NAME_NOT_IMPORTANT\n'
                         + '\tTITLE_NOT_IMPORTANT\t2.0\n'
                         + 'Amount owed is 2.0\n'
                         + 'You earned 1 frequent renter points')

    def create_rental_for(self, days_rented, price_code):
        movie = self.get_movie(price_code)
        rental = Rental(movie, days_rented)
        return rental

    def get_movie(self, price_code):
        if price_code == Movie.REGULAR:
            return RegularMovie(TITLE)
        if price_code == Movie.NEW_RELEASE:
            return NewReleaseMovie(TITLE)
        if price_code == Movie.CHILDRENS:
            return ChildrenMovie(TITLE)
        else:
            return None

    def test_statement_for_new_release_movie(self):
        #arrange
        self.customer.add_rental(self.create_rental_for(1, Movie.NEW_RELEASE))

        #assert
        self.assertEqual(self.customer.statement(),
                         'Rental Record for NAME_NOT_IMPORTANT\n'
                         + '\tTITLE_NOT_IMPORTANT\t3.0\n'
                         + 'Amount owed is 3.0\n'
                         + 'You earned 1 frequent renter points')

    def test_statement_for_childrens_movie_rental_more_than_3_days(self):
        #arrange
        self.customer.add_rental(self.create_rental_for(4, Movie.CHILDRENS))

        #assert
        self.assertEqual(self.customer.statement(),
                         'Rental Record for NAME_NOT_IMPORTANT\n'
                         + '\tTITLE_NOT_IMPORTANT\t3.0\n'
                         + 'Amount owed is 3.0\n'
                         + 'You earned 1 frequent renter points')

    def test_statement_for_childrens_movie_rental_more_than_4_days(self):
        #arrange
        self.customer.add_rental(self.create_rental_for(3, Movie.CHILDRENS))

        #assert
        self.assertEqual(self.customer.statement(),
                         'Rental Record for NAME_NOT_IMPORTANT\n'
                         + '\tTITLE_NOT_IMPORTANT\t1.5\n'
                         + 'Amount owed is 1.5\n'
                         + 'You earned 1 frequent renter points')

    def test_statement_for_new_release_movie_rental_more_than_1_day(self):
        # arrange
        self.customer.add_rental(self.create_rental_for(2, Movie.NEW_RELEASE))

        # assert
        self.assertEqual(self.customer.statement(),
                         'Rental Record for NAME_NOT_IMPORTANT\n'
                         + '\tTITLE_NOT_IMPORTANT\t6.0\n'
                         + 'Amount owed is 6.0\n'
                         + 'You earned 2 frequent renter points')

    def test_statement_for_few_movie_rental(self):
        # arrange
        self.customer.add_rental(self.create_rental_for(1, Movie.REGULAR))
        self.customer.add_rental(self.create_rental_for(4, Movie.NEW_RELEASE))
        self.customer.add_rental(self.create_rental_for(4, Movie.CHILDRENS))

        # assert
        self.assertEqual(self.customer.statement(),
                         'Rental Record for NAME_NOT_IMPORTANT\n'
                         + '\tTITLE_NOT_IMPORTANT\t2.0\n'
                         + '\tTITLE_NOT_IMPORTANT\t12.0\n'
                         + '\tTITLE_NOT_IMPORTANT\t3.0\n'
                         + 'Amount owed is 17.0\n'
                         + 'You earned 4 frequent renter points')

    def test_statement_for_regular_movie_rental_more_than_5_day(self):
        # arrange
        movie = self.get_movie(Movie.REGULAR)
        movie.set_price_code(Movie.REGULAR)
        self.customer.add_rental(Rental(movie, 5))

        # assert
        self.assertEqual(self.customer.statement(),
                         'Rental Record for NAME_NOT_IMPORTANT\n'
                         + '\tTITLE_NOT_IMPORTANT\t6.5\n'
                         + 'Amount owed is 6.5\n'
                         + 'You earned 1 frequent renter points')
