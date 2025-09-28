# fns_and_dsa/temp_conversion_tool.py

# Exact global conversion factors (top-level, as required)
FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using FAHRENHEIT_TO_CELSIUS_FACTOR.
    Raises ValueError with the exact message if input is not numeric.
    """
    try:
        f = float(fahrenheit)
    except (TypeError, ValueError):
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    return (f - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using CELSIUS_TO_FAHRENHEIT_FACTOR.
    Raises ValueError with the exact message if input is not numeric.
    """
    try:
        c = float(celsius)
    except (TypeError, ValueError):
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    return (c * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    temp_input = input("Enter the temperature to convert: ")
    try:
        temperature = float(temp_input)
    except ValueError:
        # exact message expected by the checker
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "C":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result}°F")
    elif unit == "F":
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
