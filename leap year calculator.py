def is_leap(year):
    if year % 4 == 0:

        if year % 100 == 0:

            if year % 400 == 0:
                print('leap year')

            else:
                print('not leap year')
        else:
            print('not leap year')
    else:
        print('not leap year')


is_leap(2025)
