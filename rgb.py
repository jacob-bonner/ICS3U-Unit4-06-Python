#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: November 2019
# This program outputs every possible RGB combination


def main():
    # This function outputs every possible RGB combination

    # Variables
    red = 0
    green = 0
    blue = 0

    # Process
    for red in range(256):
        for green in range(256):
            for blue in range(256):
                print("RGB: {0},{1},{2}".format(red, green, blue))


if __name__ == "__main__":
    main()
