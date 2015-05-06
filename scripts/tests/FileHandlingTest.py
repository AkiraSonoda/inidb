__author__ = 'Akira Sonoda'

import unittest
from Configuration import Configuration
from FileHandler import FileHandler
import os



class FileHandlingTestCase(unittest.TestCase):
    os = ["Darwin","Linux","Windows"]

    def setUp(self):
        self.config = Configuration('../tests/resources/package.ini')
        self.fileHandler = FileHandler(self.config)

    def test_copy_all_files_in_directory(self):
        self.fileHandler.copyAllFilesToTarget("akisim","patch")
        self.assertEqual(True, os.path.exists(self.fileHandler.getCurrentTargetDirectory("akisim")))

    def test_getOs(self):
        result = self.fileHandler.getOs()
        self.assertIn(result, self.os)

if __name__ == '__main__':
    unittest.main()
