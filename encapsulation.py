class car:
    def _init_(self, speed):
        self._speed = speed

    def get_speed(self):
        return self._speed

    def set_speed(self, new_speed):
        if new_speed > 0:
            self._speed = new_speed


my_car= car(60)
current_speed = my_car.get_speed()
print("current speed:", current_speed)

my_car.set_speed(75)
print("Updated speed:")
