class RideManager:
    def __init__(self) -> None:
        print("Ride manager activated")
        self.__available_cars = []
        self.__available_bikes = []
        self.__available_cngs = []

    def add_a_vehicle(self, vehical_type, vehicle) -> None:
        if vehical_type == "car":
            self.__available_cars.append(vehicle)
        elif vehical_type == "bike":
            self.__available_bikes.append(vehicle)
        else:
            self.__available_cngs.append(vehicle)

    def get_available_car(self):
        return self.__available_cars

    def find_a_vehicle(self, rider, vehical_type, destination):
        print("looking for a cat")
        if vehical_type == "car":
            if len(self.__available_cars) == 0:
                print("sorry no cars is available")
                return False
            for car in self.__available_cars:
                print("potential", rider.location, car.driver.location)
                if abs(rider.location - car.driver.location) < 10:
                    destination = abs(rider.location - destination)
                    fare = destination * car.rate
                    if rider.balance < fare:
                        print('You do not have enough money for this ride')
                        return False
                    if car.status == "available":
                        car.status = "unavailable"
                        self.__available_cars.remove(car)
                        print("find a vehicle for you", fare)
                        return True
            print("looping done")


uber = RideManager()
