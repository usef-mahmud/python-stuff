from exp_utils import * 

class Car:
    def __init__(self, brand: str) -> None:
        self.__brand = brand

    def get_brand(self) -> str:
        return self.__brand
    
    def set_brand(self, brand: str) -> None:
        self.__brand = brand

    def __repr__(self):
        return f'the brand name is {self.__brand}'

    def __add__(self, other) -> None:
        return self.__brand + ' ' + other.get_brand()

class SUV(Car):
    def __init__(self, brand: str) -> None:
        super().__init__(brand)
        

car1 = Car('BMW')
car2 = Car('Mercedes')

print(car1 + car2)