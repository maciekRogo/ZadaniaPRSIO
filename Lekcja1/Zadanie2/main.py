class MyWater:
    def __init__(self, big,medium,small):
        self.big = big
        self.medium = medium
        self.small = small

    def add_large(self,z):
        self.big += z
    def add_medium(self,x):
        self.medium += x
    def add_small(self,c):
        self.small += c
MyWater1 = MyWater(0,0,0)
a = input("Podaj ilość dużych butelek: ")
MyWater1.add_large(int(a))
a1 = input("Podaj ilość srednich butelek: ")
MyWater1.add_medium(int(a1))
a2 = input("Podaj ilość małych butelek: ")
MyWater1.add_small(int(a2))
ile = MyWater1.big*2 + MyWater1.medium + MyWater1.small*0.5
print(f"Mam teraz {ile} litrów wody\n dużych butelek: {MyWater1.big} \nśrednich butelek: {MyWater1.medium} \n małych butelek: {MyWater1.small}")
