__author__ = 'Akira Sonoda'

import configparser
import os

class Configuration:

    def __init__(self, path_to_config_file):
        self.config_filepath = os.path.abspath(path_to_config_file)
        self.config = configparser.ConfigParser()
        self.config.read(self.config_filepath)

    def getItem(self, section, item):
        return self.config[section][item]


    def setMajorVersion(self, distro, major_version_num):
        # TODO rename to increase .. major version should be numeric and therefore be possible to increase by 1
        self.config.set(distro, "major", major_version_num )

    def setMinorVersion(self, distro, minor_version_num):
        # TODO rename to increase .. minor version should be numeric and therefore be possible to increase by 1
        self.config.set(distro, "minor", minor_version_num )

    def setPatchVersion(self, distro, patch_version_num):
        # TODO rename to increase .. patch version should be numeric and therefore be possible to increase by 1
        self.config.set(distro, "patch", patch_version_num )


    def assembleVersionTag(self, distro):
        version_name = ""

        if distro == "akisim":
            version_name = self.config['Distros']['akisim_name']
        elif distro == "freaki":
            version_name = self.config['Distros']['freaki_name']
        elif distro == "arriba":
            version_name = self.config['Distros']['arriba_name']

        return (version_name + '-'
                             + self.config[version_name]['major']
                             + '.'
                             + self.config[version_name]['minor']
                             + '.'
                             + self.config[version_name]['patch'] )

