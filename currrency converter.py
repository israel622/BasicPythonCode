def main():
    print('currency converter')
    print()

    dollars = eval(input('how many dollars do you have?: '))
    pounds = convert_to_pounds(dollars)

    print('converted dollars to pounds: ', pounds)

convert_to_pounds = lambda dollars: round(dollars * 0.82)

main()