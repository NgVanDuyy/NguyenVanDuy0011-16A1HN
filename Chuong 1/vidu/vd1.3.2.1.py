class Animal:
    def __init__(self, name):
        self._name = name

    def Display(self):
        print("I'm {}".format(self._name))

class Dog(Animal):
    def __init__(self, name, size, age, color):
        super().__init__(name)
        self.size = size
        self.age = age
        self.color = color

    def Go(self, place):
        print("I'm going to {}".format(place))

obj1 = Dog("bull", "large", 2, "yellow")
obj1.Display()
obj1.Go("garden")