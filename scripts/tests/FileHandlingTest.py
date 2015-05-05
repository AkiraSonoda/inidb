__author__ = 'Akira Sonoda'

import unittest
from Configuration import Configuration
import os
from package import copyAllFiles
from package import createTargetDirectory
from package import getOs


class FileHandlingTestCase(unittest.TestCase):
    def setUp(self):
        self.config = Configuration('../tests/resources/package.ini')
        self.operatingSystem = getOs()

    def test_create_target_directory(self):
        self.config.increaseNumber("akisim","patch")
        target_directory_path = self.config.getItem(self.operatingSystem,'src_root') + '/target/' + self.config.assembleVersionTag("akisim")
        createTargetDirectory(target_directory_path)
        self.assertEqual(True, os.path.exists(target_directory_path))
        # cleanup
        os.rmdir(target_directory_path)
        self.assertEqual(False, os.path.exists(target_directory_path))

    def test_copy_all_files_in_directory(self):
        self.config.increaseNumber("akisim","patch")
        target_directory_path = self.config.getItem(self.operatingSystem,'src_root') + '/target/' + self.config.assembleVersionTag("akisim")
        createTargetDirectory(target_directory_path)

        source_directory_path = self.config.getItem(self.operatingSystem, "akisim")
        copyAllFiles(source_directory_path,target_directory_path)
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
