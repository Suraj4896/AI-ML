from abc import ABC, abstractmethod

#abstract class
class Animal(ABC):
    @abstractmethod
    def make_sound():
        pass

#child class
class Lion(Animal):
    def make_sound(self):
        print('Roar...')

lion = Lion()
lion.make_sound()