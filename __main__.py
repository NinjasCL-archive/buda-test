#!/usr/bin/env python3
import sys

from src import Metro, Train


def getArgs():
    if len(sys.argv) < 3:
        raise Exception("usage: <origin> <destination> <color?>")

    # origin destination
    if len(sys.argv) < 4:
        return (sys.argv[1], sys.argv[2], None)

    # origin destination color
    if len(sys.argv) >= 4:
        return (sys.argv[1], sys.argv[2], sys.argv[3])


def main():
    try:
        origin, destination, color = getArgs()

        metro = Metro.fromJson()
        train = Train.new(metro).color(color).origin(origin).to(destination).travel()

        print(train)

    except Exception as e:
        print(e)
        raise e


if __name__ == "__main__":
    main()
