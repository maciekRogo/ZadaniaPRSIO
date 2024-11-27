"""Napisz klasę Employee , która dziedziczy po klasie Person i dodaje dodatkowy atrybut
position (stanowisko) oraz nadpisuje metodę introduce() , tak aby zwracała: "Cześć,
mam na imię <name> i pracuję jako <position>" . Użyj super() w metodzie
introduce() , aby wywołać metodę z klasy Person ."""
class Person:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        return f"Cześć, mam na imie {self.name}"
class Employee(Person):
    def __init__(self, name, position):
        super().__init__(name)
        self.position = position
    def introduce(self):
        print( f"{super().introduce()} i pracuję jako {self.position}")
pracownik = Employee("Kamil","Wędkarz")
pracownik.introduce()