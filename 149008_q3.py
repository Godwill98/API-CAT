# Base Vehicle class
class Vehicle:
    def __init__(self, registration_number, make, model):
        self.registration_number = registration_number
        self.make = make
        self.model = model

    def display_info(self):
        return f"Registration Number: {self.registration_number}, Make: {self.make}, Model: {self.model}"

# Car class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, registration_number, make, model, number_of_seats):
        super().__init__(registration_number, make, model)
        self.number_of_seats = number_of_seats

    def display_info(self):
        return f"{super().display_info()}, Number of Seats: {self.number_of_seats}"

# Truck class inheriting from Vehicle
class Truck(Vehicle):
    def __init__(self, registration_number, make, model, cargo_capacity):
        super().__init__(registration_number, make, model)
        self.cargo_capacity = cargo_capacity

    def display_info(self):
        return f"{super().display_info()}, Cargo Capacity: {self.cargo_capacity} tons"

# Motorcycle class inheriting from Vehicle
class Motorcycle(Vehicle):
    def __init__(self, registration_number, make, model, engine_capacity):
        super().__init__(registration_number, make, model)
        self.engine_capacity = engine_capacity

    def display_info(self):
        return f"{super().display_info()}, Engine Capacity: {self.engine_capacity} cc"

# Fleet class to manage the fleet
class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Vehicle with registration number {vehicle.registration_number} added successfully.")

    def display_all_vehicles(self):
        if not self.vehicles:
            print("No vehicles in the fleet.")
        else:
            for vehicle in self.vehicles:
                print(vehicle.display_info())

    def search_vehicle_by_registration_number(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                print(vehicle.display_info())
                return
        print(f"No vehicle found with registration number {registration_number}.")

# Demonstration of functionalities
def main():
    fleet = Fleet()

    while True:
        print("\nTransport Fleet Management System")
        print("1. Add a new vehicle")
        print("2. Display all vehicles")
        print("3. Search for a vehicle by registration number")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            v_type = input("Enter vehicle type (car, truck, motorcycle): ").lower()
            registration_number = input("Enter registration number: ")
            make = input("Enter make: ")
            model = input("Enter model: ")

            if v_type == 'car':
                number_of_seats = int(input("Enter number of seats: "))
                vehicle = Car(registration_number, make, model, number_of_seats)
            elif v_type == 'truck':
                cargo_capacity = float(input("Enter cargo capacity in tons: "))
                vehicle = Truck(registration_number, make, model, cargo_capacity)
            elif v_type == 'motorcycle':
                engine_capacity = int(input("Enter engine capacity in cc: "))
                vehicle = Motorcycle(registration_number, make, model, engine_capacity)
            else:
                print("Invalid vehicle type. Please try again.")
                continue
            
            fleet.add_vehicle(vehicle)

        elif choice == '2':
            fleet.display_all_vehicles()
        elif choice == '3':
            registration_number = input("Enter registration number: ")
            fleet.search_vehicle_by_registration_number(registration_number)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
