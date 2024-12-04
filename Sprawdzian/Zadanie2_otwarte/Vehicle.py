from abc import ABC, abstractmethod


class Vehicle:
    def __init__(self, registration_number, capacity,
                 current_location=(0, 0)) -> None:
        self.registration_number = registration_number
        self.capacity = capacity
        self.current_location = current_location

    @abstractmethod
    def move(self, destination):
        pass

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def calculate_fuel_cost(self, distance):
        pass

