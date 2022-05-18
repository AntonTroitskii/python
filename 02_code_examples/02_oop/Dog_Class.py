class Dog:
    #Class Attributes
    species = 'mammal'
    is_hungry = False

    def __str__(self):
        return self.description()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        self.is_hungry = True

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


#
# # Instantiate the Dog object
# philo = Dog("Philo", 5)
# mikey = Dog("Mikey", 6)
#
# # Access the instance attributes
# print("{} is {} and {} is {}.".format(
#     philo.name, philo.age, mikey.name, mikey.age))
#
# # Is Philo a mammal?
# if philo.species == "mammal":
#     print("{0} is a {1}!".format(philo.name, philo.species))
#
# print(philo.speak("Гав-гав"))
# print(philo.description())
#
# # Child classes inherit attributes and
# # behaviors from the parent class
# jim = Bulldog("Jim", 12)
# print(jim.description())
#
# # Child classes have specific attributes
# # and behaviors as well
# # дочерний класс имеет свои атрибуты
# print(jim.run("slowly"))
#
# # Is jim an instance of Dog()?
# print(isinstance(jim, Dog))
#
# # Is julie an instance of Dog()?
# julie = Dog("Julie", 100)
# print(isinstance(julie, Dog))
#

# # Is johnny walker an instance of Bulldog()
# johnnywalker = RussellTerrier("Johnny Walker", 4)
# print(isinstance(johnnywalker, Bulldog))
# # Is julie and instance of jim?
# # print(isinstance(julie, jim))

# print("The_Dog class is running")