#! /usr/bin/env python3

__author__ = 'Akira Sonoda'

import sys, os
import Configuration
import shutil

distros = ["akisim","freaki","arriba"]
versions = ["major","minor","patch"]

def main(argv):

    if not plausi(argv):
        SystemExit(1)

    distro = argv[1].lower()
    version = argv[2].lower()

    configuration = Configuration("./resources/package.ini")
    operatingSystem = getOs()
    # increase Version Number
    name_package = configuration.getItem('Distros',distro)
    configuration.increaseNumber(name_package, version)

    # Create target directory
    target_directory_path = configuration.getItem(operatingSystem,'src_root') + '/target/' + configuration.assembleVersionTag(name_package)

    # get the source path of the given distro.
    source_directory_path = configuration.getItem(operatingSystem,distro)

    # Copy all Files into the target directory
    copyAllFiles(source_directory_path, target_directory_path)

    # remove the git files

    # copy the grid-specific default ini files

    # copy the scripts files ( not sure maybe we create a different distribution channel )

    # tar.gz the whole stuff

    # install the tar.gz on repo server


    SystemExit(0)


def plausi(argv):
    # TODO accept an option which indicates what Version to increase.

    if len(argv) != 3:
        usage()
        return False

    distro = argv[1]
    version = argv[2]

    if distro.lower() not in distros:
        usage()
        return False

    if version.lower() not in versions:
        usage()
        return False

    return True

def usage():
    print("package.py [distribution] [grid]")
    print('           [distribution] is one of "akisim", "freaki", "arriba" ')
    print('           [version] is one of "majnor", "minor", "patch" ')


if __name__ == "__main__":
    main(sys.argv)