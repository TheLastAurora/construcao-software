from abc import *
import random
import inspect
from itertools import ifilter


class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractclassmethod
    def make_sound(self):
        pass

class Cachorro(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print("au au.")
    
    def run(self):
        print("running.")

class Cavalo(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def run(self):
        print("running.")

    
    def make_sound(self):
        print("hiin in in hinir.")
    
    def run(self):
        print("running.")


class Preguica(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def make_sound():
        print("ai ai.")

    def climb_tree(self):
        print("climbing tree.")

class AnimalTeste():

    def __init__(self) -> None:
        veloz, fumaca, cafe = Cavalo("Veloz", 6), Cachorro("Fumaca", 3), Preguica("Café", 5)
        for animal in (veloz, fumaca, cafe):
            animal.make_sound()

class Veterinario():

    def __init__(self) -> None:
        pass

    def exam(self, animal):
        animal.make_sound()

class Zoologico():
    cage = [Animal(random.choice(["Rajado, Fumaca, Parágrafo, Inácio"]), random.randint(1, 20)) for animal in 10*Animal.__subclasses__()]

    def expo(self):
        for animal in self.cage:
            attrs = (getattr(animal, name) for name in dir(animal))
            methods = ifilter(inspect.ismethod, attrs)  
            for method in methods:
                try:
                    method()
                except TypeError:
                    pass
                

    def __init__(self) -> None:
        pass       

class AnimalInvalidoException(Exception):
    '''Tipo de Animal Inválido'''


try: 
    cavalo = Cavalo('Pé de pano', 10)
    preguica = Preguica('Velcidade', 5)
    cachorro = Cachorro('Peludin', 8)
    if not isinstance(cavalo, Animal):
        raise AnimalInvalidoException
    if not isinstance(preguica, Animal):
        raise AnimalInvalidoException
    if not isinstance(cachorro, Animal):
        raise AnimalInvalidoException
except AnimalInvalidoException as e:
    print(e.message)
