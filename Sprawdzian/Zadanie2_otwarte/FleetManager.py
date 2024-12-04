from Vehicle import Vehicle

class FleetManager:
    def __init__(self):
        self.fleet = []

    def add_vehicle(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            raise TypeError("Dodawany obiekt musi być instancją klasy pochodnej od Vehicle.")
        self.fleet.append(vehicle)
        print(f"Pojazd {vehicle.registration_number} dodany do floty.")

    def dispatch(self, vehicle_id, destination):
        for vehicle in self.fleet:
            if vehicle.registration_number == vehicle_id:
                try:
                    vehicle.move(destination)
                except ValueError as e:
                    print(f"Błąd: {e}")
                return
        print(f"Nie znaleziono pojazdu o numerze rejestracyjnym {vehicle_id}.")

    def get_summary(self):
        print("Podsumowanie floty:")
        for vehicle in self.fleet:
            print(vehicle.get_info())
    def calculate_total_fuel_cost(self, distance):
        total_cost = 0
        for vehicle in self.fleet:
            total_cost += vehicle.calculate_fuel_cost(distance)
        print(f"Całkowity koszt paliwa dla dystansu {distance} km: {total_cost:.2f} złotych.")
        return total_cost

