"""
Napisz klasę TemperatureConverter , która będzie miała:
metodę klasową from_celsius_to_fahrenheit(cls, temp) , która zamienia
temperaturę w stopniach Celsjusza na Fahrenheita.
metodę statyczną from_fahrenheit_to_celsius(temp) , która zamienia temperaturę
z Fahrenheita na Celsjusza.

Użyj metody klasowej do konwersji z Celsjusza na Fahrenheita.
Użyj metody statycznej do konwersji z Fahrenheita na Celsjusza.
"""
class TemperatureConverter:
    @classmethod
    def from_celsius_to_fahrenheit(cls,temp):
        return temp * 9/5 + 32
    @staticmethod
    def from_fahrenheit_to_celsius(temp):
        return (temp - 32) * 5/9
print(TemperatureConverter.from_fahrenheit_to_celsius(273))
print(TemperatureConverter.from_celsius_to_fahrenheit(0))


