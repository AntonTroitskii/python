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



class Pets:

    def __init__(self, dogs: []):
        self.list_dog = dogs


    def about1(self):
        print("I have {} dogs".format(len(self.list_dog)))
        for i in self.list_dog:
            print(i)
        print("And they're all mammals, of course.")


    def about2(self):
        self.about1()
        are_my_dogs_hungry = False
        for i in self.list_dog:
            if i.is_hungry:
                are_my_dogs_hungry = True

        if are_my_dogs_hungry:
            print("My dogs are hungry")
        else:
            print("My dogs are not hungry")


def pets_test1():
    dogs = [
        ("Tom", 6),
        Dog("Fletcher", 7),
        Dog("Larry", 7)
    ]

    pets = Pets(dogs)
    pets.about1()


def pets_test2():
    dogs = [
        ("Tom", 6),
        Dog("Fletcher", 7),
        Dog("Larry", 7)
    ]
    pets = Pets(dogs)
    pets.about2()


pets_test2()
