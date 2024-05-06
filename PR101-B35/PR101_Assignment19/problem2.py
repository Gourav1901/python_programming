# Write two functions named celsiusToFahrenheit and fahrenheitToCelsius to convert between Celsius and Fahrenheit.
# Use the functions to convert a given temperature.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


celsius_temperature = 36
fahrenheitToTemperature = celsius_to_fahrenheit(celsius_temperature)
print(f"{celsius_temperature} degrees Celsius is equal to {fahrenheitToTemperature:.2f} degrees Fahrenheit.")

fahrenheitToTemperature = 79
celsius_temperature = fahrenheit_to_celsius(fahrenheitToTemperature)
print(f"{fahrenheitToTemperature} degrees Fahrenheit is equal to {celsius_temperature:.2f} degrees Celsius.")

