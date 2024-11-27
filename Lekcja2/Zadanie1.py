"""Napisz klasę Person , która będzie miała atrybut name i metodę introduce() , która zwraca
tekst: "Cześć, mam na imię <name>" . Następnie stwórz klasę Student , która dziedziczy
po klasie Person i ma dodatkowy atrybut student_id oraz nadpisuje metodę
introduce() , aby zwracała tekst: "Cześć, mam na imię <name> i jestem studentem z
numerem <student_id>" ."""

class Person:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        return f"Cześć, mam na imie {self.name}"
class Student(Person):
    def __init__(self, name, student_id):
        Person.__init__(self, name)
        self.student_id = student_id
    student_id = 12323432413
    def introduce(self):
        return f"Cześć, mam na imie {self.name} i jestem studentem z numerem {self.student_id}"
uczen = Student("Kamil","12432432")
print(uczen.introduce())