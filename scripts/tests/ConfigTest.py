__author__ = 'Akira Sonoda'

import unittest

from Configuration import Configuration
from package import getOs

class ConfigTestCase(unittest.TestCase):

    def setUp(self):
        self.config = Configuration('../tests/resources/package.ini')

    def test_load_config(self):
        distros_akisim_name = self.config.getItem('Distros','akisim_name')
        self.assertEqual(distros_akisim_name, 'Aki')

    def test_assemble_version(self):
        version_name = self.config.assembleVersionTag("akisim")
        self.assertEqual(version_name, 'Aki-15.0.0')

    def test_set_major_number(self):
        self.config.setMajorVersion("Aki","16")
        version_name = self.config.assembleVersionTag("akisim")
        self.assertEqual(version_name, 'Aki-16.0.0')

    def test_set_minor_number(self):
        self.config.setMinorVersion("Aki","1")
        version_name = self.config.assembleVersionTag("akisim")
        self.assertEqual(version_name, 'Aki-15.1.0')

    def test_set_patch_number(self):
        self.config.setPatchVersion("Aki","1")
        version_name = self.config.assembleVersionTag("akisim")
        self.assertEqual(version_name, 'Aki-15.0.1')

    def test_set_minor_patch_number(self):
        self.config.setPatchVersion("Aki","1.7")
        version_name = self.config.assembleVersionTag("akisim")
        self.assertEqual(version_name, 'Aki-15.0.1.7')

    def test_getOs(self):
        result = getOs()
        self.assertEquals(result, "Darwin")

if __name__ == '__main__':
    unittest.main()
