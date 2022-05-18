from Dog_Class import Dog


def get_biggest_number(* args):
    return max(args)


dog1 = Dog('dog1', 20)
dog2 = Dog('dog2', 30)
dog3 = Dog('dog3', 40)


print(dog1, dog2, dog3)
max_age = get_biggest_number(dog1.age, dog2.age, dog3.age)
print("The oldest dog is {} years old".format(max_age))
