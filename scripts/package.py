#! /usr/bin/env python3

__author__ = 'Akira Sonoda'

import sys
import os
import Configuration
import shutil

distros = ["akisim","freaki","arriba"]
grids = ["dereos","metropolis","osgrid"]

def main(argv):

    if not plausi(argv):
        SystemExit(1)

    distro = argv[1].lower()
    grid = argv[2].lower()

    configuration = Configuration("./resources/package.ini")
    operatingSystem = getOs()
    # increase Version Number


    # Create target directory
    createTargetDirectory(configuration.getItem(operatingSystem,'src_root'))

    # Copy all Files into the target directory
    copyAllFiles(distro)

    # remove the git files

    # copy the grid-specific default ini files

    # copy the scripts files ( not sure maybe we create a different distribution channel )

    # tar.gz the whole stuff

    # install the tar.gz on repo server


    SystemExit(0)

def createTargetDirectory(directoryPath):
    os.mkdir(directoryPath)


def copyAllFiles(distro):
    pass

def getOs():
    result = os.uname()
    return(result[0])


def plausi(argv):
    # TODO accept an option which indicates what Version to increase.

    if len(argv) != 3:
        usage()
        return False

    distro = argv[1]
    grid = argv[2]

    if distro.lower() not in distros:
        usage()
        return False

    if grid.lower() not in grids:
        usage()
        return False

    return True

def usage():
    print("package.py [distribution] [grid]")
    print('           [distribution] is one of "akisim", "freaki", "arriba" ')
    print('           [grids] is one of "dereos", "metropolis", "osgrid" ')


if __name__ == "__main__":
    main(sys.argv)