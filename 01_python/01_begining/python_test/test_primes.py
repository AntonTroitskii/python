from unittest import TestCase

from python_test.primes import is_prime


class Test(TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(5))

    def test_is_not_prime(self):
        self.assertTrue(is_prime(6))
