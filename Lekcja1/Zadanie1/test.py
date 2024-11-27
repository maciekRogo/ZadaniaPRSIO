class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


Car1 = Car("niebieski", 20000)
Car2 = Car("czerwony", 30000)

print(
    f"Samochów {Car1.color} ma przejechane {Car1.mileage} mil,a samochów {Car2.color} ma przejechane {Car2.mileage} mil.")
