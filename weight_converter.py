# Python wight converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (kg or lbs): ")

if unit.lower() == 'kg':
    weight = weight * 2.205
    unit = 'lbs'
elif unit.lower() == 'lbs':
    weight = weight / 2.205
    unit = 'kg'
else:
    print(f"{unit} is not valid")

print(f"Your weight is: {round(weight, 2)} {unit}")