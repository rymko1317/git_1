from abc import ABC, abstractmethod

class Pet(ABC):
    def __init__(self, age, owner, name):
        self.age = age
        if not owner or not name:
            raise ValueError("enter the name and owner")
        self.owner = owner
        self.name = name


    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError("Cannot be negative")
        self._age = value

    @abstractmethod
    def voice(self):
        pass

class Dog(Pet):
    def voice(self):
        print("voice dog")

class Cat(Pet):
    def voice(self):
        print("voice cat")

class Parrot(Pet):
    def voice(self):
        print("voice parrot")

dog = Dog(3, "owner", "name")

dog.voice()
print(dog.age, dog.name, dog.owner)