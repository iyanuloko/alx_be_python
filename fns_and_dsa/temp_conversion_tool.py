FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


while True:
    temperature = input("Enter the temperature to convert: ")
    try:
        temperature = int(temperature)
        break
    except:
        print("Enter a numeric temperature value.")
temp_scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()
if temp_scale == "c":
    result = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {result}°F")
elif temp_scale == "f":
    result = convert_to_celsius(temperature)
    print(f"{temperature}°F is {result}°C")
else:
    print("Invalid unit.")
