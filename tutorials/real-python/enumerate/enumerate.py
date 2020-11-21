# !/bin/python

if __name__ == "__main__":

    values = ['a', 'b', 'c']

    print('enumerate starting at default of zero')
    for count, value in enumerate(values):
        print(count, value)

    print('\nenumerate starting at 108')
    for count, value in enumerate(values, start=108):
        print(count, value)

