from unittest import TestCase

from src.prime_number import is_prime


class TestPrimeNumber(TestCase):
    def setUp(self) -> None:
        self.correct_prime_number = '73'
        self.not_prime_number = '168'
        self.negative_number = '-15'
        self.text = '+abcdef'

    def test_correct_prime_number(self):
        result = is_prime(self.correct_prime_number)
        self.assertTrue(result)

    def test_not_prime_number(self):
        result = is_prime(self.not_prime_number)
        self.assertFalse(result)

    def test_negative_number(self):
        result = is_prime(self.negative_number)
        self.assertFalse(result)

    def test_if_raises_error_with_string_input(self):
        self.assertRaises(ValueError, is_prime, self.text)

