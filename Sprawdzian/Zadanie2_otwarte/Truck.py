from Vehicle import Vehicle


class Truck(Vehicle):
    MAX_DISTANCE = 800
    FUEL_COST_PER_KM = 1.5
    EXTRA_CARGO_COST_PER_KM = 0.05

    def __init__(self, registration_number, capacity, current_location=(0, 0),
                 cargo=[]):
        super().__init__(registration_number=registration_number,
                         capacity=capacity,
                         current_location=current_location)
        self.cargo = cargo

        if len(self.cargo) > self.capacity:
            raise ValueError(f"Ładunek przekracza maksymalną ładowność ({self.capacity}). Usuń część ładunku.")

    def move(self, destination):
        distance = ((destination[0] - self.current_location[0]) ** 2 + (
                    destination[1] - self.current_location[1]) ** 2) ** 0.5

        if distance > self.MAX_DISTANCE:
            raise ValueError(
                f"Ciężarówka nie może pokonać dystansu {distance: .2f} km w jednym przejeździe. Maksymalny dystans: {self.MAX_DISTANCE} km.")

        self.current_location = destination
        print(f"Ciężarówka {self.registration_number} przemieściła się do {destination}.")

    def calculate_fuel_cost(self, distance):
        total_cargo_weight = len(self.cargo)  # Przyjmujemy, że każdy ładunek waży 1 tonę (dla uproszczenia)

        base_fuel_cost = distance * self.FUEL_COST_PER_KM
        extra_cargo_cost = distance * total_cargo_weight * self.EXTRA_CARGO_COST_PER_KM
        total_cost = base_fuel_cost + extra_cargo_cost

        return total_cost

    def get_info(self):
        cargo_list = ", ".join(self.cargo) if self.cargo else "Brak ładunku"
        return (f"Truck: {self.registration_number}\n"
                f"  Lokalizacja: {self.current_location}\n"
                f"  Ładowność: {self.capacity}\n"
                f"  Ładunek: {cargo_list}\n")

