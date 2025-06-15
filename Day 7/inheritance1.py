
class Animal:
    def __init__(self,name, isHervibore):
        self.name = name
        self.isHervibore = isHervibore
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
    def eatsPlan(self):
        if(self.isHervibore):
            print(f"{self.name} eats plant")
        else:
            print(f"{self.name} doesn't eat plant")

class Dog(Animal):
    def __init__(self,breed, name,isHerbivore):
        super().__init__(name, isHerbivore)
        self.breed = breed
    def make_sound(self):
        print(f"{self.name} is barking")
    def print_breed(self):
        print(f"{self.name} is {self.breed} dog")
    def fetch_bone(self):
        print(f"{self.name} fetched a bone")

class Cat(Animal):
    def __init__(self, breed, name,isHerbivore): #initialize attributes breed name and is herbivore from the class animal
        super().__init__(name,isHerbivore)
        self.breed = breed

    def make_sound(self):
        print(f"{self.name} is saying meow")
    def print_breed(self):
        print(f"{self.name} is {self.breed} cat")

cat1 = Cat("Kaley","Tom",True)

cat1.make_sound()
cat1.eat()
cat1.sleep()
cat1.eatsPlan()

dog1 = Dog("German Shepher", "Max",False)
dog1.sleep()
dog1.make_sound()
dog1.fetch_bone()
