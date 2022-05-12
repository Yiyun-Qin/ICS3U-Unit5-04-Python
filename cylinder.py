#!/usr/bin/env python3

# Created by Yiyun Qin
# Created in May 2022
# This is the math program, calculating the area of the triangle

import math


def VolumeCylinder(radius, height):
    # This function calculates the area of the triangle

    # process
    volume = math.pi * pow(radius, 2) * height

    # output
    return volume


def main():
    # This function does try and catch, input and output
    print("This function calculates the volume of the cylinder.")
    print("Please enter the radius and the height.")
    print("")

    # input
    radius_string = input("Enter the radius of the cylinder (cm): ")
    height_string = input("Enter the height of the cylinder (cm): ")

    # process & output
    print("")
    try:
        radius_integer = int(radius_string)
        height_integer = int(height_string)
        # call functions
        volume = VolumeCylinder(radius=radius_integer, height=height_integer)
        print(
            "The volume of this cylinder with the radius of {0} cm and the height of {1} cm is {2:,.2f} cm².".format(
                radius_string, height_string, volume
            )
        )
    except Exception:
        print("Invalid number!")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
