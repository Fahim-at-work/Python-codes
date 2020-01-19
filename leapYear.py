while True:
    try:
        check_year = int(input("Enter a year: "))
        if check_year < 0:
            raise ValueError
        break
    except ValueError as val_err:
        print("Please enter a positive number ")


def check_if_leap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{0} is a leap year".format(year))
            else:
                print("{0} is not a leap year".format(year))
        else:
            print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))


check_if_leap(check_year)
