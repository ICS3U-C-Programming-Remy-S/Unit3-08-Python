#!/usr/bin/env python3
# Created by: Remy Skelton
# Created on: Oct 15, 2023
# This program will ask the user
# for their year and it will tell them
# if it is a leap year or not with try catch


def main():
    # Get the user year as a string and display message about program
    print("This program will ask the user for their year and it will tell them")
    print("if it is a leap year or not with try catch.")
    user_year_as_string = input("Please enter your year: ")

    # Catch if the user year is something wrong
    try:
        # Convert user year as a string to int
        user_year_as_int = int(user_year_as_string)

        # calculate remainder to determine if leap year
        leap_year_4 = user_year_as_int % 4
        leap_year_100 = user_year_as_int % 100
        leap_year_400 = user_year_as_int % 400

        # Check if leap_year_4 leaves a remainder
        if leap_year_4 == 0:
            # Check if leap_year_100 does not leave a remainder
            if leap_year_100 != 0:
                print("{} is a leap year.".format(user_year_as_int))
            else:
                # Check if leap_year_400 leaves a remainder
                if leap_year_400 == 0:
                    print("{} is a leap year.".format(user_year_as_int))
                else:
                    print(
                        "{} is how many years until the next leap year.".format(
                            leap_year_4
                        )
                    )

        # Display if the year is not a leap year
        else:
            print(
                "{} is how many years until the next leap year.".format(4 - leap_year_4)
            )

    # Display a message to the user if they entered something that is not valid
    except Exception:
        # Message for invalid user input
        print("\n{} is not a valid age.".format(user_year_as_int))


if __name__ == "__main__":
    main()
