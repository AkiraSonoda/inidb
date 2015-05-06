__author__ = 'Akira Sonoda'

import os
import shutil

IGNORE_PATTERNS = ('.git','.nant','.gitignore','.hgignore')

class FileHandler:

    def __init__(self, configuration):
        self.config = configuration

    def getCurrentTargetDirectory(self, distro):
        return(self.config.getItem(self.getOs(),'src_root') +os.sep+ 'target'+os.sep+ self.config.assembleVersionTag(distro))

    def copyAllFilesToTarget(self, distro, level ):
        self.config.increaseNumber(distro,level)
        target_directory_path = self.config.getItem(self.getOs(),'src_root') +os.sep+ 'target' +os.sep+ self.config.assembleVersionTag(distro)
        source_directory_path = self.config.getItem(self.getOs(), distro) + os.sep
        shutil.copytree(source_directory_path, target_directory_path, symlinks=True, ignore=shutil.ignore_patterns(*IGNORE_PATTERNS))

    def getOs(self):
        result = os.uname()
        return(result[0])
