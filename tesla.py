class Tesla:
    # WRITE YOUR CODE HERE
    def __init__(self, model: str, color: str, autopilot: bool = False,
                 efficiency: float = 0.3):
        self.__model = model
        self.__color = color
        self.__battery_charge = 99.9
        self.__is_locked = True
        self.__seats_count = 5
        self .__autopilot = autopilot
        self.__efficiency = efficiency
    
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, new_color: str) -> None:
        self._color = new_color

    @property
    def seats_count(self) -> str:
        return self.__seats_count
    
    @seats_count.setter
    def seats_count(self, new_count) -> None:
        if new_count < 2:
            print("Seats count cannot be lower than 2!")
            return
        self.__seats_count = new_count

    @property
    def is_locked(self) -> str:
        return self.__is_locked

    def unlock(self) -> None:
        self.__is_locked = False

    def lock(self) -> None:
        self.__is_locked = True

    def open_doors(self) -> str:
        if self.__is_locked:
            return "Car is locked!"
        return "Doors opens sideways"

    def check_battery_level(self) -> str:
        return f"Battery charge level is {self.__battery_charge}%"
 
    def charge_battery(self):
        self.__battery_charge = 100
        self.check_battery_level()

    def drive(self, travel_range: float):
        battery_discharge_percent = travel_range * self.__efficiency
        if self.__battery_charge - battery_discharge_percent >= 0:
            # ADD YOUR CODE
            self.__battery_charge -= battery_discharge_percent
            return self.check_battery_level()
        else:
            return self.check_battery_level()

    def welcome(self) -> str:
        return f"Hello from {self.__model}!"

    def autopilot(self, obsticle: str) -> str:
        if self.__autopilot:
            return f"Tesla model {self.__model} avoids {obsticle}"
        else:
            return "Autopilot is not available"