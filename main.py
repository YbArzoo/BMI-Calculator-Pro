print("Welcome to the BMI Calculator.")
print("Created by - YB Zoop")
print("How do you want to give your height in? Meters or Feet? Answer in m for Meters or in f for feet.")
user = str(input(""))

if user == "m":
    height = float(input("Enter your height in m: "))
    weight = float(input("Enter your weight in kg: "))

    bmi = round((weight) / (height * height))

    if bmi < 18.5:
        print(f"Your BMI is {bmi}, you are underweight.")
    elif bmi < 25:
        print(f"Your BMI is {bmi}, you have a normal weight.")
    elif bmi < 30:
        print(f"Your BMI is {bmi}, you are slightly overweight.")
    elif bmi < 35:
        print(f"Your BMI is {bmi}, you are obese.")
    else:
        print(f"Your BMI is {bmi}, you are clinically obese.")

elif user == "f":
    print("If your height is 5 feet 5 inch you should enter 5 only, inch part comes a bit later.")
    feet = float(input("Enter your height in feet only: "))
    inch = float(input("Enter the inch now: "))
    feet_inch = (feet * 0.3048) + (inch * 0.0254)
    print("Your height in meters", feet_inch)
    weight_2 = float(input("Enter your weight in kg: "))

    height_2 = float(feet_inch)

    bmi_2 = round((weight_2 / (height_2 ** 2)))

    if bmi_2 < 18.5:
        print(f"Your BMI is {bmi_2}, you are underweight.")
    elif bmi_2 < 25:
        print(f"Your BMI is {bmi_2}, you have a normal weight.")
    elif bmi_2 < 30:
        print(f"Your BMI is {bmi_2}, you are slightly overweight.")
    elif bmi_2 < 35:
        print(f"Your BMI is {bmi_2}, you are obese.")
    else:
        print(f"Your BMI is {bmi_2}, you are clinically obese.")

print("Thank you for using BMI CALCULATOR PRO.")
