from Vehicle import Vehicle



class Bus(Vehicle):
    MAX_DISTANCE = 800
    FUEL_COST_PER_KM = 1.25
    PASSENGER_WEIGHT_FACTOR = 0.02

    def __init__(self, registration_number, capacity, current_location=(0, 0), passenger_list=[]):
        super().__init__(registration_number, capacity, current_location)
        self.passenger_list = passenger_list if passenger_list else []
        if len(self.passenger_list) > self.capacity:
            raise ValueError(f"Przekroczono maksymalną liczbę pasażerów ({self.capacity}).")

    def move(self, destination):

        distance = ((destination[0] - self.current_location[0]) ** 2 + (
                    destination[1] - self.current_location[1]) ** 2) ** 0.5
        if distance > self.MAX_DISTANCE:
            raise ValueError(
                f"Autobus nie może pokonać dystansu {distance: .2f} km w jednym przejeździe. Maksymalny dystans: {self.MAX_DISTANCE} km.")

        self.current_location = destination
        print(f"Autobus {self.registration_number} przemieścił się do {destination}.")

    def calculate_fuel_cost(self, distance):
        # Koszt paliwa uwzględnia liczbę pasażerów
        base_fuel_cost = distance * self.FUEL_COST_PER_KM
        extra_cost = distance * len(self.passenger_list) * self.PASSENGER_WEIGHT_FACTOR
        total_cost = base_fuel_cost + extra_cost
        return total_cost

    def get_info(self):
        passenger_names = ", ".join(self.passenger_list) if self.passenger_list else "Brak pasażerów"
        return (f"Bus: {self.registration_number}\n"
                f"  Lokalizacja: {self.current_location}\n"
                f"  Pojemność: {self.capacity}\n"
                f"  Pasażerowie: {passenger_names}\n")

