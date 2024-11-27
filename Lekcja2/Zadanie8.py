"""Stwórz klasy FlyingAnimal i SwimmingAnimal z odpowiednimi metodami fly() oraz
swim() . Następnie stwórz klasę Duck , która dziedziczy zarówno po FlyingAnimal , jak i
SwimmingAnimal , implementując swoje wersje metod fly() i swim() . Dodaj do klasy
Duck metodę introduce() .
Następnie napisz funkcję, która przyjmuje listę różnych obiektów (np. kaczki, ptaki, ryby) i
wywołuje na każdym obiekcie odpowiednie metody ( fly() , swim() , introduce() ),
pokazując, jak działa polimorfizm z wielodziedziczeniem.

Klasa Duck dziedziczy po dwóch klasach ( FlyingAnimal i SwimmingAnimal ).
Metody fly() , swim() i introduce() są odpowiednio zaimplementowane w klasie
Duck .
"""
class FlyingAnimal:
    def fly(self):
        print(f"Latam")
class SwimmingAnimal:
    def swim(self):
        print("Pływam")
class Duck(FlyingAnimal, SwimmingAnimal):
    def __init__(self):
        pass
    def introduce(self):
        print("Jestem kaczką")

class Ryba(FlyingAnimal, SwimmingAnimal):
    def __init__(self):
        pass
    def introduce(self):
        print("Jestem rybą")
def introduce_all(animals):
    for animal in animals:
        animal.introduce()
        animal.fly()
        animal.swim()
        print("-"*20)
animals = [Duck(), Ryba()]
introduce_all(animals)



