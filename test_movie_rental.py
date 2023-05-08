from unittest import TestCase
from customer import Customer, Rental, Movie

class Tests(TestCase):
    def test_return_new_customer(self):
        customer = Customer('NAME_NOT_IMPORTANT')
        self.assertIsNotNone(customer)
