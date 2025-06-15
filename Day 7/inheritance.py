#make a base class vehicle
#make two child classes bike and car
#use attributs that can be similar in both class and make some function that are unique and same

class vehicle:
    def __init__(self,engine,milage,):
        self.engine = engine
        self.milage = milage
        
    def start_engine(self):
        print(f"{self.engine}is started")

    def check_milage(self):
        print(f"the milage given by the vehicle is {self.milage}")

   
class bike(vehicle):
    def __init__(self,engine,milage ,model):
        super().__init__(engine ,milage) #initialize engine and milage from parent class vehicle
        self.model = model
    def what_model(self):
        print(f"the model of the bike is {self.model}")

class car(vehicle):
    def __init__(self,engine,milage,color):
        super().__init__(engine,milage)
        self.color = color

    def check_color(self):
        print("the color of the car is {self.color}")

car1 = car("v12","12kmpl","red")
bike1 = bike("800cc","30kmpl","2025")



car1.check_milage()
bike1.what_model()
