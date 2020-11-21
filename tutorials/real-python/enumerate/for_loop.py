# !/bin/python3

if __name__ == "__main__":
    print('\nloop over iterable')
    values = ['a', 'b', 'c']
    for val in values:
        print(val)

    print('\nuse range and len to create index and loop')
    for i in range(len(values)):
        print(i, values[i])

    print('\nmaintain counter while looping')
    counter = 0
    for val in values:
        print(counter, val)
        counter += 1
