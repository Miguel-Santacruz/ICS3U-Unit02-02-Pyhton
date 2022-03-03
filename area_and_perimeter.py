#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: March 2022
# This program calculates area and perimeter of a rectangle
#   with length and width inputted by the user


def main():
    # this function calculates area and perimeter

    # input
    Length = int(input("Enter length of the rectangle (cm): "))
    Width = int(input("Enter width of the rectangle (cm): "))

    # process
    area = Length * Width
    perimeter = 2 * (Length + Width)

    # output
    print("")
    print("Its area is {0} cm².".format(area))
    print("Its perimeter is {0} cm.".format(perimeter))

    print("\nDone.")


if __name__ == "__main__":
    main()
