
print()
print("Weight converter across kilograms and pounds")
print()

w = float(input("Enter your weight: "))
u = input("Enter the unit (kg for kilograms and lbs for pounds): ")

if u.lower() == "kg":
    c = w*2.205
    print("Weight in pounds is "+str(c))
elif u.lower() == "lbs":
    c = w/2.205
    print("Weight in kilograms is "+str(c))
else:
    print("Please enter a valid input")
