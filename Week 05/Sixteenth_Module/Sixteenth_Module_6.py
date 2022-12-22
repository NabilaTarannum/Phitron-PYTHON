class RideManager:
    def __init__(self) -> None:
        print("Ride manager activated")
        self.__income = 0
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
        print("looking for a car")
        if vehical_type == "car":
            if len(self.__available_cars) == 0:
                print("sorry no cars is available")
                return False
            for car in self.__available_cars:
                # print("potential", rider.location, car.driver.location)
                if abs(rider.location - car.driver.location) < 10:
                    destination = abs(rider.location - destination)
                    fare = destination * car.rate
                    if rider.balance < fare:
                        print(
                            "You do not have enough money for this trip.",
                            fare,
                            rider.balance,
                        )
                        return False
                    if car.status == "available":
                        car.status = "unavailable"
                        self.__available_cars.remove(car)
                        rider.start_a_trip(fare)
                        car.driver.start_a_trip(destination, fare * 0.8)
                        self.__income += fare * 0.2
                        print(f"vehicle for {rider.name} for fare: {fare} with {car.driver.name}")
                        return True
            print("looping done")


uber = RideManager()
