class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def __str__(self):
        return f"hello, my name is {self.name}, i am {self.age} years old, and am a {self.gender}"
class Introduction(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

person1 = Introduction("samuel", 20, "male")
print(person1)