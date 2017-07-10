# Write a asmall program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to on an 18-30 holiday (they must be
# over 18 and under 30).
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.

if __name__ == "__main__":
    name = input("What is your name? ")
    age = int(input("What is your age? "))

    if age >= 18 and age <= 30:
        print("Welcome to the holiday!")
    else:
        print("Sorry, but you can't come.")
