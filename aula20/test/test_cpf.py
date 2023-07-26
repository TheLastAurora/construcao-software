import unittest
from src.ValidaCPF import ValidaCPF


class TestValidaCPF(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.validator = ValidaCPF()

    def test_valid_cpf(self):
        self.assertTrue(self.validator.is_cpf("84629513047"))

    def test_invalid_cpf_all_same_digits(self):
        self.assertFalse(self.validator.is_cpf("22222222222"))

    def test_invalid_cpf_less_than_11_digits(self):
        self.assertFalse(self.validator.is_cpf("8374836721"))

    def test_invalid_cpf_more_than_11_digits(self):
        self.assertFalse(self.validator.is_cpf("273846591037"))

    def test_invalid_cpf_non_digit_characters(self):
        self.assertFalse(self.validator.is_cpf("957410Z2835"))

    def test_valid_cpf_with_leading_zeros(self):
        self.assertTrue(self.validator.is_cpf("00100200304"))

    def test_type(self):
        self.assertFalse(self.validator.is_cpf(14329413057))

    def test_empty_string_input(self):
        self.assertFalse(self.validator.is_cpf(""))

    def test_none_input(self):
        self.assertFalse(self.validator.is_cpf(None))


if __name__ == '__main__':
    unittest.main()
