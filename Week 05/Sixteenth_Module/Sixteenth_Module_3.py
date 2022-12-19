import hashlib
from random import randint
from Sixteenth_Module_4 import BRTA
from Sixteenth_Module_5 import Car, Bike, Cng
from Sixteenth_Module_6 import uber


class UserAlreadyExists(Exception):
    def __init__(self, email, *args: object) -> None:
        print(f"user: {email} already exists.")
        super().__init__(*args)


license_authority = BRTA()


class User:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email

        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        already_exists = False
        with open("Week 05/Sixteenth_Module/users.txt", "r") as file:
            if email in file.read():
                already_exists = True
                # raise UserAlreadyExists(email)
        file.close()
        if not already_exists:
            with open("users.txt", "a") as file:
                file.write(f"{email} {pwd_encrypted}\n")
            file.close()
        print(self.name, "user created")

    @staticmethod
    def log_in(email, password):
        stored_password = ""
        with open("users.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    stored_password = line.split(" ")[1]
        file.close()

        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if hashed_password == stored_password:
            print("valid user password")
            return True
        else:
            print("invalid user password")
            return False
        # print(f"password found {stored_password}")


class Rider(User):
    def __init__(self, name, email, password, location, balance) -> None:
        super().__init__(name, email, password)
        self.location = location
        self.balance = balance

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def request_trip(self, destination):
        pass

    def start_a_trip(self, fare):
        self.balance -= fare


class Driver(User):
    def __init__(self, name, email, password, location, license) -> None:
        super().__init__(name, email, password)
        self.location = location
        self.license = license
        self.valid_driver = license_authority.validate_license(email, license)
        self.earning = 0

    def take_driving_test(self):
        result = license_authority.take_driving_test(self.email)
        if result == False:
            print("Sorry you failed, try again")
        else:
            self.license = result
            self.valid_driver = True

    def register_a_vehicle(self, vehicle_type, license_plate, rate):
        if self.valid_driver is True:
            if vehicle_type == "car":
                new_vehicle = Car(vehicle_type, license_plate, rate, self)
            elif vehicle_type == "bike":
                new_vehicle = Bike(vehicle_type, license_plate, rate, self)
            else:
                new_vehicle = Cng(vehicle_type, license_plate, rate, self)
            uber.add_a_vehicle(vehicle_type, new_vehicle)
        else:
            print("Your are not a valid driver")

    def start_a_trip(self, destination, fare):
        self.earning += fare
        self.location = destination


""" hero = User("Hero Alom", "hero@alom.com", "heroOhHero")
User.log_in("hero@alom.com", "heroOhHero")

kuber = Driver("Kuber Maji", "kuber@maji.com", "kopilaJaisna", 54, 4556)

result = license_authority.validate_license(kuber.email, kuber.license)
print(result)
kuber.take_driving_test()
result = license_authority.validate_license(kuber.email, kuber.license)
print(result) """

rider1 = Rider("rider1", "rider1@gmail.com", "rider1", randint(0, 100), 5000)
rider2 = Rider("rider2", "rider2@gmail.com", "rider2", randint(0, 100), 5000)
rider3 = Rider("rider3", "rider3@gmail.com", "rider3", randint(0, 100), 5000)

for i in range(1, 100):
    driver1 = Driver(
        f"driver {i}",
        f"driver{i}@gmail.com",
        f"driver{i}",
        randint(0, 100),
        randint(1000, 9999),
    )
    driver1.take_driving_test()
    driver1.register_a_vehicle("car", randint(10000, 99999), 10)

uber.find_a_vehicle(rider1, "car", 90)
print(uber.get_available_car())
