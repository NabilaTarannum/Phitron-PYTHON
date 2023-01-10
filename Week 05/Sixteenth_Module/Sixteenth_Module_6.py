""" rider_manager.py """


class RideManager:
    def __init__(self) -> None:
        print("Ride manager activated")
        self.__income = 0
        self.__trip_history = []
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

    def total_income(self):
        return self.__income

    def trip_history(self):
        return self.__trip_history

    def find_a_vehicle(self, rider, vehical_type, destination):
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
                        trip_info = f"Vehicle for {rider.name} for fare: {fare} with {car.driver.name} started: {rider.location} to: {destination}"
                        self.__available_cars.remove(car)
                        rider.start_a_trip(fare, trip_info)
                        car.driver.start_a_trip(rider.location, destination, fare * 0.8, trip_info)
                        self.__income += fare * 0.2
                        self.__trip_history.append(trip_info)
                        print(trip_info)
                        return True
            print("looping done")


uber = RideManager()
