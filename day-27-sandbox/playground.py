def add(*args):
    a = 0
    for n in args:
        a += n
    return a

print(add(1,2,3,4))


def calculate(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key, value)

calculate(add=3, multiply=5)

class Car:

    def __init__(self, **kwargs):
        """
        Create a car
        :param kwargs:
        :keyword str brand: kwarg 1
        :keyword str model: kwarg 1
        """
        print(kwargs)
        self.brand = kwargs.get("brand")
        self.model = kwargs.get("model")

my_car = Car(brand="Ford", model="Ranger")
print(my_car.model)
