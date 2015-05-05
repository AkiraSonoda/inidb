__author__ = 'Akira Sonoda'

import unittest
import re

from Configuration import Configuration
from package import getOs

class ConfigTestCase(unittest.TestCase):

    def setUp(self):
        self.config = Configuration('../tests/resources/package.ini')

    def test_load_config(self):
        distros_akisim_name = self.config.getItem('Distros','akisim')
        self.assertEqual(distros_akisim_name, 'Aki')

    def test_assemble_version(self):
        version_name = self.config.assembleVersionTag("akisim")
        match = re.search('(.*)-\d*\.\d*\.\d*', version_name)
        if match:
            distro_name = match.group(1)
        self.assertEqual(distro_name, 'Aki')

    def test_increase_major_number(self):
        version_name = self.config.assembleVersionTag("akisim")
        match = re.search('.*-(\d*)\.(\d*)\.(\d*)', version_name)
        if match:
            old_version_number = match.group(1)

        self.config.increaseNumber("akisim","major")
        version_name = self.config.assembleVersionTag("akisim")
        match = re.search(".*-(\d*)\.(\d*)\.(\d*)", version_name)
        if match:
            new_version_number = match.group(1)
        self.assertEqual(int(new_version_number), int(old_version_number)+1)

    def test_increase_minor_number(self):
        version_name = self.config.assembleVersionTag("akisim")
        match = re.search('.*-(\d*)\.(\d*)\.(\d*)', version_name)
        if match:
            old_version_number = match.group(2)

        self.config.increaseNumber("akisim","minor")
        version_name = self.config.assembleVersionTag("akisim")
        match = re.search(".*-(\d*)\.(\d*)\.(\d*)", version_name)
        if match:
            new_version_number = match.group(2)
        self.assertEqual(int(new_version_number), int(old_version_number)+1)

    def test_increase_patch_number(self):
        version_name = self.config.assembleVersionTag("akisim")
        match = re.search('.*-(\d*)\.(\d*)\.(\d*)', version_name)
        if match:
            old_version_number = match.group(3)

        self.config.increaseNumber("akisim","patch")
        version_name = self.config.assembleVersionTag("akisim")
        match = re.search(".*-(\d*)\.(\d*)\.(\d*)", version_name)
        if match:
            new_version_number = match.group(3)
        self.assertEqual(int(new_version_number), int(old_version_number)+1)

    def test_getOs(self):
        result = getOs()
        self.assertEquals(result, "Darwin")

if __name__ == '__main__':
    unittest.main()
