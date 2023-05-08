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