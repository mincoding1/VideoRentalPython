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

