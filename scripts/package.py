#! /usr/bin/env python3

__author__ = 'Akira Sonoda'

import sys, getopt

distros = ["akisim","freaki","arriba"]
grids = ["dereos","metropolis","osgrid"]

def main(argv):
    plausi(argv)

    SystemExit(0)


def plausi(argv):
    if len(argv) != 2:
        print("package.py [distribution] [grid]")
        print('           [distribution] is one of "akisim", "freaki", "arriba" ')
        print('           [grids] is one of "dereos", "metropolis", "osgrid" ')
        return False

    distro = argv[0]
    grid = argv[1]

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