#! /usr/bin/env python3

__author__ = 'Akira Sonoda'

import sys
import configparser
import os

distros = ["akisim","freaki","arriba"]
grids = ["dereos","metropolis","osgrid"]

def main(argv):
    if not plausi(argv):
        SystemExit(1)

    configuration = loadConfig(os.path.abspath('resources/package.ini'))

    SystemExit(0)

def loadConfig(filepath):
    print(filepath)
    config = configparser.ConfigParser()
    config.read(filepath)
    return(config)


def plausi(argv):
    if len(argv) != 3:
        print("package.py [distribution] [grid]")
        print('           [distribution] is one of "akisim", "freaki", "arriba" ')
        print('           [grids] is one of "dereos", "metropolis", "osgrid" ')
        return False

    distro = argv[1]
    grid = argv[2]

    if distro.lower() not in distros:
        print("package.py [distribution] [grid]")
        print('           [distribution] is one of "akisim", "freaki", "arriba" ')
        print('           [grids] is one of "dereos", "metropolis", "osgrid" ')
        return False

    if grid.lower() not in grids:
        print("package.py [distribution] [grid]")
        print('           [distribution] is one of "akisim", "freaki", "arriba" ')
        print('           [grids] is one of "dereos", "metropolis", "osgrid" ')
        return False

    return True


if __name__ == "__main__":
    main(sys.argv)