


class Mammals:
    number_of_legs=4#class attribute

    def __init__(self,species,color):
        self.species=species
        self.color=color

    def __del__(self):
        print("")
    def walk(self):#class method
        self.has_tails=True#instance attribute
        print(f"walking with {self.number_of_legs}legs")
    @staticmethod#static methos
    def eat():
        print("eating through mouth")



dog=Mammals("dog","black")
cat=Mammals("cat","brown")
print(dog.number_of_legs)
print(cat.number_of_legs)
print(cat.color)
print(dog.color)
print(dog.species)
cat.eat()
dog.eat()
#self depends on instance
class Dog(Mammals):
    number_of_legs=5
    def how_many_legs(self):
        return self.number_of_legs
dog=Dog
print(dog.how_many_legs())