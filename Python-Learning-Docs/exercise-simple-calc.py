# temperature unit conversion

print("TEMPERATURE CONVERSION PROGRAM")

celcius = float(input("Enter the temperature in Celsius: "))
print(f'celcius: {celcius} C')

## reamur
reamur = 4 / 5 * celcius
print(f'reamur: {reamur} R')

## fahrenheit
fahrenheit = 9 / 5 * celcius + 32
print(f'fahrenheit: {fahrenheit} F')

## kelvin
kelvin = celcius + 273.15
print(f'kelvin: {kelvin} K')