FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR 
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    temperature = int(input("Enter the temperature to convert: "))
    unit_of_measurement = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if unit_of_measurement == "C":
        temperature_in_celsius = convert_to_celsius(temperature)
        print(f"{temperature}°F is {temperature_in_celsius}°C")
    elif unit_of_measurement == "F":
        temperature_in_fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {temperature_in_fahrenheit}°F")
    else:
        print("Invalid unit of measurement.")


if __name__ == "__main__":
    main()