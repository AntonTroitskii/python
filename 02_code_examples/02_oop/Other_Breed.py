class Dog:
    species = 'mammal'

class SomeBreed(Dog):
    pass

class SomeOtherBreed(Dog):
    species = 'reptile'

frank = SomeBreed()
print(frank.species)

beans = SomeOtherBreed()
print(beans.species)
