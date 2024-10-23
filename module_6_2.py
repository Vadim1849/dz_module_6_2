class Vehicle:
    __COLOR_VARIANTS = ['red', 'yellow', 'orange', 'green', 'purple']
    def get_color_variants(self):
        return self.__COLOR_VARIANTS

    # Методы get_model, get_horsepower, get_color находятся в одном классе с соответствующими им атрибутами:
    # Атрибуты будут доступны для методов __model, __engine_power, __color.
    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        # Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color,
        # если он есть в списке __COLOR_VARIANTS.
        if new_color.lower() in [color.lower() for color in self.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehicle):
    __PASSENGER_LIMIT = 5  # В седан может поместиться только 5 пассажиров

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)

    def get_passenger_limit(self):
        return self.__PASSENGER_LIMIT

vehicle = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle.print_info()
vehicle.set_color('Pink')
vehicle.set_color('Orange')
vehicle.owner = 'Vasyok'

vehicle.print_info()