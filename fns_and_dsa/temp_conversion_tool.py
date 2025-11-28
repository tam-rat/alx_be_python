# temp_conversion_tool.py

# ---- Global Conversion Factors ----
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9      # For (F - 32) * 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5      # For (C * 9/5) + 32


# ---- Conversion Functions ----

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


# ---- Main Program Logic ----

def main():
    # Get temperature input
    temperature_input = input("Enter the temperature to convert: ").strip()

    # Validate numeric input
    try:
        temperature = float(temperature_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Get unit input
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # Determine conversion
    if unit == "F":
        celsius = convert_to_celsius(temperature)
        print(f"{temperature}°F is {celsius}°C")

    elif unit == "C":
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {fahrenheit}°F")

    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


if __name__ == "__main__":
    main()
