""" Kalkulačka BMI: Vytvorte jednoduchú kalkulačku telesnej hmotnosti (BMI) pomocou Pythonu. Používateľ zadá svoju hmotnosť a výšku, a program vypočíta a vypíše BMI hodnotu. 
BMI = m/h²

m = telesná hmotnosť v kilogramoch
h = telesná výška v metroch
Underweight: BMI less than 18.5
Normal weight: BMI 18.5-24.9
Overweight: BMI 25-29.9
Obesity (Class I): BMI 30-34.9
Severe obesity (Class II): BMI 35-39.9
Morbid obesity (Class III): BMI 40 or higher
"""

import time

print("Welcome")

time.sleep(0.15)

name = input("Please give me your name: ")

print(f"Hello {name}, I'm calculator for BMI.")

time.sleep(0.5)

print("\nBody Mass Index (BMI) is a person’s weight in kilograms divided by the square of height in meters.")

time.sleep(0.5)

m = float(input("\nYour weight is (kg)?: "))
h = float(input("Your height is (cm)?: "))

print(f"\nYour weight is {m} kg.")
print(f"Your height is {h} cm.\n")

time.sleep(1)

def bmi(m, h):
    bmi = round(m / ((h / 100) ** 2))
    print(f"Your BMI is: {bmi}\n")
    if bmi < 18.5:
        print(f"{name} has underweight.")
    elif bmi >= 18.5 and bmi <= 24.9:
        print(f"{name} has normal weight.")
    elif bmi >= 25.0 and bmi <= 29.9:
        print(f"{name} has overweight.")
    elif bmi >= 30.0 and bmi <= 34.9:
        print(f"{name} has obesity (class I).")
    elif bmi >= 35.0 and bmi <= 39.9:
        print(f"{name} has obesity (class II).")
    else:
        print(f"{name} has obesity (class III).")
bmi(m, h)




""" import time

def get_input(prompt):
    return input(prompt)

def calculate_bmi(m, h):
    return round(m / ((h / 100) ** 2))

def print_bmi_category(name, bmi):
    bmi_ranges = [
        (18.5, "has underweight"),
        (24.9, "has normal weight"),
        (29.9, "has overweight"),
        (34.9, "has obesity (class I)"),
        (39.9, "has obesity (class II)"),
        (float('inf'), "has obesity (class III)")
    ]

    for max_bmi, category in bmi_ranges:
        if bmi <= max_bmi:
            print(f"{name} {category}")
            break

print("Welcome")
time.sleep(0.15)

name = get_input("Please give me your name: ")
print(f"Hello {name}, I'm calculator for BMI.")
time.sleep(0.5)

print("\nBody Mass Index (BMI) is a person’s weight in kilograms divided by the square of height in meters.")
time.sleep(0.5)

m = float(get_input("\nYour weight is (kg)?: "))
h = float(get_input("Your height is (cm)?: "))

print(f"\nYour weight is {m} kg.")
print(f"Your height is {h} cm.\n")
time.sleep(1)

bmi = calculate_bmi(m, h)
print(f"Your BMI is: {bmi}\n")
print_bmi_category(name, bmi) """



