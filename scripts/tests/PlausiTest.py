__author__ = 'akira'

import unittest
from package import plausi

arguments_ok = ["package.py", "akisim", "dereos"]
arguments_too_few = ["package.py", "akisim"]
arguments_too_many = ["package.py", "akisim", "dereos", "another"]
arguments_empty = []
arguments_wrong_distro = ["package.py","vanilla", "dereos"]
arguments_ok_upper = ["package.py", "Akisim", "Dereos"]
arguments_nok_grid = ["package.py", "Akisim", "Avination"]


class PlausiTestCase(unittest.TestCase):
    def test_correct_number_of_arguments(self):
        result = plausi(arguments_ok)
        self.assertEqual(result, True)

    def test_too_few_number_of_arguments(self):
        result = plausi(arguments_too_few)
        self.assertEqual(result, False)

    def test_too_many_number_of_arguments(self):
        result = plausi(arguments_too_many)
        self.assertEqual(result, False)

    def test_empty_number_of_arguments(self):
        result = plausi(arguments_empty)
        self.assertEqual(result, False)

    def test_wrong_distro_argument(self):
        result = plausi(arguments_wrong_distro)
        self.assertEqual(result, False)

    def test_uppercase_argument(self):
        result = plausi(arguments_ok_upper)
        self.assertEqual(result, True)

    def test_uppercase_argument(self):
        result = plausi(arguments_nok_grid)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
