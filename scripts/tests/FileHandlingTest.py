__author__ = 'Akira Sonoda'

import unittest
from package import copyAllFiles


class FileHandlingTestCase(unittest.TestCase):
    def test_copy_all_files_in_directory(self):
        copyAllFiles("akisim")
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
