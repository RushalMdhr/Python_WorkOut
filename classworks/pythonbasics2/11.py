'''11. Create a Python script that converts temperature from 
Fahrenheit to Celsius and vice versa, based on user input'''

temp = float(input("Enter the temperature: "))
unit = input("Is this in Fahrenheit (F) or Celsius (C)? ").upper()

if unit == "F":
    celsius = (temp - 32) * 5/9
    print(f"{temp}°F is {celsius:.2f}°C")
elif unit == "C":
    fahrenheit = (temp * 9/5) + 32
    print(f"{temp}°C is {fahrenheit:.2f}°F")
else:
    print("Invalid unit")
