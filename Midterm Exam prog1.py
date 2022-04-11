def main():
    class TemperatureConversion:

        def __init__(self, temp=1):
            self._temp = temp

    class CelsiusToFahrenheit(TemperatureConversion):

        def conversion(self):
            return (self._temp * 9) / 5 + 32

    class CelsiusToKelvin(TemperatureConversion):

        def conversion(self):
            return self._temp + 273.15

    class KelvinToCelsius(TemperatureConversion):

        def conversion(self):
            return self._temp - 273.15

    class FahrenheitToCelsius(TemperatureConversion):

        def conversion(self):
            return (self._temp - 32) * 5 / 9

    tempInCelsius = float(input("Enter the temperature in Celsius: "))
    tempInFahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    tempInKelvin = float(input("Enter the temperature in Kelvin: "))

    convert = CelsiusToKelvin(tempInCelsius)

    print("Celsius to Kelvin")
    print(str(convert.conversion()) + " Kelvin")

    convert = CelsiusToFahrenheit(tempInCelsius)
    print("Celsius to Fahrenheit")
    print(str(convert.conversion()) + " Fahrenheit")

    convert = FahrenheitToCelsius(tempInFahrenheit)
    print("Fahrenhiet to Celsius")
    print(str(convert.conversion()) + " Celsius")

    convert = KelvinToCelsius(tempInCelsius)
    print("Kelvin to Celsius")
    print(str(convert.conversion()) + " Celsius")


main()

