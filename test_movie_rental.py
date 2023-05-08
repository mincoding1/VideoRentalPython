from unittest import TestCase
from customer import Customer, Rental, Movie

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
        movie = Movie(TITLE, Movie.REGULAR)
        days_rented = 2
        rental = Rental(movie, days_rented)
        self.customer.add_rental(rental)

        #assert
        self.assertEqual(self.customer.statement(),
                         'Rental Record for NAME_NOT_IMPORTANT\n'
                         + '\tTITLE_NOT_IMPORTANT\t2.0\n'
                         + 'Amount owed is 2.0\n'
                         + 'You earned 1 frequent renter points')

    def test_statement_for_new_release_movie(self):
        #arrange
        movie = Movie(TITLE, Movie.NEW_RELEASE)
        days_rented = 1
        rental = Rental(movie, days_rented)
        self.customer.add_rental(rental)

        #assert
        self.assertEqual(self.customer.statement(),
                         'Rental Record for NAME_NOT_IMPORTANT\n'
                         + '\tTITLE_NOT_IMPORTANT\t3.0\n'
                         + 'Amount owed is 3.0\n'
                         + 'You earned 1 frequent renter points')

    def test_statement_for_childrens_movie_rental_more_than_3_days(self):
        #arrange
        movie = Movie(TITLE, Movie.CHILDRENS)
        days_rented = 4
        rental = Rental(movie, days_rented)
        self.customer.add_rental(rental)

        #assert
        self.assertEqual(self.customer.statement(),
                         'Rental Record for NAME_NOT_IMPORTANT\n'
                         + '\tTITLE_NOT_IMPORTANT\t3.0\n'
                         + 'Amount owed is 3.0\n'
                         + 'You earned 1 frequent renter points')

    def test_statement_for_childrens_movie_rental_more_than_4_days(self):
        #arrange
        movie = Movie(TITLE, Movie.CHILDRENS)
        days_rented = 3
        rental = Rental(movie, days_rented)
        self.customer.add_rental(rental)

        #assert
        self.assertEqual(self.customer.statement(),
                         'Rental Record for NAME_NOT_IMPORTANT\n'
                         + '\tTITLE_NOT_IMPORTANT\t1.5\n'
                         + 'Amount owed is 1.5\n'
                         + 'You earned 1 frequent renter points')

    def test_statement_for_new_release_movie_rental_more_than_1_day(self):
        # arrange
        movie = Movie(TITLE, Movie.NEW_RELEASE)
        days_rented = 2
        rental = Rental(movie, days_rented)
        self.customer.add_rental(rental)

        # assert
        self.assertEqual(self.customer.statement(),
                         'Rental Record for NAME_NOT_IMPORTANT\n'
                         + '\tTITLE_NOT_IMPORTANT\t6.0\n'
                         + 'Amount owed is 6.0\n'
                         + 'You earned 2 frequent renter points')

    def test_statement_for_few_movie_rental(self):
        # arrange
        regular_movie = Movie(TITLE, Movie.REGULAR)
        new_release_movie = Movie(TITLE, Movie.NEW_RELEASE)
        childrens_movie = Movie(TITLE, Movie.CHILDRENS)
        self.customer.add_rental(Rental(regular_movie, 1))
        self.customer.add_rental(Rental(new_release_movie, 4))
        self.customer.add_rental(Rental(childrens_movie, 4))

        # assert
        self.assertEqual(self.customer.statement(),
                         'Rental Record for NAME_NOT_IMPORTANT\n'
                         + '\tTITLE_NOT_IMPORTANT\t2.0\n'
                         + '\tTITLE_NOT_IMPORTANT\t12.0\n'
                         + '\tTITLE_NOT_IMPORTANT\t3.0\n'
                         + 'Amount owed is 17.0\n'
                         + 'You earned 4 frequent renter points')
