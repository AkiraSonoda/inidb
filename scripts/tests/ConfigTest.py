__author__ = 'Akira Sonoda'

import unittest
import os.path
import configparser

from package import loadConfig


class ConfigTestCase(unittest.TestCase):
    def test_load_config(self):
        pfad = os.path.abspath('../resources/package.ini')
        config = loadConfig(pfad)
        distros_akisim_name = config['Distros']['akisim_name']
        self.assertEqual(distros_akisim_name, 'Aki')


if __name__ == '__main__':
    unittest.main()
