# !/bin/python
"""Conditionally operate on only a certain index in an iterable"""

if __name__ == "__main__":
    users = ["Test User", "Real User 1", "Real User 2"]

    print("special handling for first user")
    for index, user in enumerate(users):
        if index == 0:
            print("Extra verbose output for user: ", end='')
        print(index, user)

    print("\nprint only every second user")
    for index, user in enumerate(users):
        if index % 2 == 0:
            print(index, user)
