name = 'Eric M. Bragas'
my_age = 24
height = 74
weight = 180
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

height_cm = height * 2.54
weight_kilo = weight * 0.453592

print(f"Let's talk about {name}.")
print(f"He's {height_cm} centimeters tall.")
print(f"He's {weight_kilo} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee")

total = my_age + height + weight
print(f"If I add {my_age}, {height_cm}, and {weight_kilo} I get {total}.")
