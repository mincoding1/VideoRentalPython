from unittest import TestCase
from customer import Customer, Rental, Movie

class Tests(TestCase):
    def test_return_new_customer(self):
        customer = Customer('NAME_NOT_IMPORTANT')
        self.assertIsNotNone(customer)

    def test_statement_for_no_rental(self):
        #arrange
        customer = Customer('NAME_NOT_IMPORTANT')

        #act
        statement = customer.statement()

        #assert
        self.assertEqual(statement,
                'Rental Record for NAME_NOT_IMPORTANT\n'
                + 'Amount owed is 0\n'
                + 'You earned 0 frequent renter points')

    def test_statement_for_regular_movie_rental_for_less_than_3_days(self):
        #arrange
        customer = Customer('NAME_NOT_IMPORTANT')
        movie = Movie('TITLE_NOT_IMPORTANT', Movie.REGULAR)
        days_rented = 2
        rental = Rental(movie, days_rented)
        customer.add_rental(rental)

        #act
        statement = customer.statement()

        #assert
        self.assertEqual(statement,
                'Rental Record for NAME_NOT_IMPORTANT\n'
                + '\tTITLE_NOT_IMPORTANT\t2.0\n'
                + 'Amount owed is 2.0\n'
                + 'You earned 1 frequent renter points')

    def test_statement_for_new_release_movie(self):
        #arrange
        customer = Customer('NAME_NOT_IMPORTANT')
        movie = Movie('TITLE_NOT_IMPORTANT', Movie.NEW_RELEASE)
        days_rented = 1
        rental = Rental(movie, days_rented)
        customer.add_rental(rental)

        #act
        statement = customer.statement()

        # assert
        self.assertEqual(statement,
                'Rental Record for NAME_NOT_IMPORTANT\n'
                + '\tTITLE_NOT_IMPORTANT\t3.0\n'
                + 'Amount owed is 3.0\n'
                + 'You earned 1 frequent renter points')

    def test_statement_for_childrens_movie_rental_more_than_3_days(self):
        #arrange
        customer = Customer('NAME_NOT_IMPORTANT')
        movie = Movie('TITLE_NOT_IMPORTANT', Movie.CHILDRENS)
        days_rented = 4
        rental = Rental(movie, days_rented)
        customer.add_rental(rental)

        #act
        statement = customer.statement()

        # assert
        self.assertEqual(statement,
                 'Rental Record for NAME_NOT_IMPORTANT\n'
                 + '\tTITLE_NOT_IMPORTANT\t3.0\n'
                 + 'Amount owed is 3.0\n'
                 + 'You earned 1 frequent renter points')

    def test_statement_for_childrens_movie_rental_more_than_4_days(self):
        #arrange
        customer = Customer('NAME_NOT_IMPORTANT')
        movie = Movie('TITLE_NOT_IMPORTANT', Movie.CHILDRENS)
        days_rented = 3
        rental = Rental(movie, days_rented)
        customer.add_rental(rental)

        #act
        statement = customer.statement()

        # assert
        self.assertEqual(statement,
                'Rental Record for NAME_NOT_IMPORTANT\n'
                + '\tTITLE_NOT_IMPORTANT\t1.5\n'
                + 'Amount owed is 1.5\n'
                + 'You earned 1 frequent renter points')
