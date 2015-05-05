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

    def increaseNumber(self, distro, level):
        version_name = self.config['Distros'][distro]
        version_string = self.config[version_name][level]
        version_number = int(version_string) + 1
        self.config.set(version_name,level,str(version_number))
        with open(self.config_filepath,'w') as configfile:
            self.config.write(configfile)

    def assembleVersionTag(self, distro):

        version_name = self.config['Distros'][distro]

        return (version_name + '-'
                             + self.config[version_name]['major']
                             + '.'
                             + self.config[version_name]['minor']
                             + '.'
                             + self.config[version_name]['patch'] )

