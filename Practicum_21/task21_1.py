class AirConditioning:
    def __init__(self):
        self.__status = False
        self.__temperature = None

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        if value:
            if not self.__status:
                self.__status = True
                self.__temperature = 18
        else:
            if self.__status:
                self.__status = False
                self.__temperature = None

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if self.__status and 0 <= value <= 43:
            self.__temperature = value

    def switch_on(self):
        if not self.__status:
            self.__status = True
            self.__temperature = 18

    def switch_off(self):
        if self.__status:
            self.__status = False
            self.__temperature = None

    def reset(self):
        if self.__status:
            self.__temperature = 18

    def get_temperature(self):
        return self.__temperature

    def raise_temperature(self):
        if self.__status and self.__temperature is not None:
            if self.__temperature < 43:
                self.__temperature += 1

    def lower_temperature(self):
        if self.__status and self.__temperature is not None:
            if self.__temperature > 0:
                self.__temperature -= 1

    def __str__(self):
        if not self.__status:
            return "Кондиционер выключен."
        else:
            return f"Кондиционер включен. Температурный режим: {self.__temperature} градусов."


conditioning = AirConditioning()
print(conditioning)
print(conditioning.temperature)
print(conditioning.status)
conditioning.status = True
print(conditioning)
print(conditioning.status)
conditioning.temperature = 20
print(conditioning.temperature)
conditioning.reset()
print(conditioning)
print(conditioning.get_temperature())
conditioning.raise_temperature()
print(conditioning.get_temperature())
conditioning.lower_temperature()
print(conditioning.get_temperature())
conditioning.switch_on()
print(conditioning)
print(conditioning.get_temperature())
print(conditioning.temperature)
conditioning.temperature = 30
print(conditioning.temperature)
conditioning.status = False
print(conditioning)
for _ in range(16):
    conditioning.lower_temperature()
print(conditioning.get_temperature())
for _ in range(5):
    conditioning.lower_temperature()
print(conditioning.get_temperature())
for _ in range(40):
    conditioning.raise_temperature()
print(conditioning)
for _ in range(5):
    conditioning.raise_temperature()
print(conditioning)
conditioning.switch_off()
print(conditioning)