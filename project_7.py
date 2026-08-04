class Vehicle:
    def__init__(self,brand,max_speed)
    self.brand=brand
    self.max_speed=max_speed
    def show_details(self):
        print("Brand",self.brand)
        print("Max_Speed",self.max_speed)
class car(Vehicle):
    def__init__(self,model,seats,brand,max_speed)
    self.model=model
    self.seats=seats
    super().__init__(brand,max_speed)
    def show_details(self):
        print("Model",model)
        print("Seats",seats)
        super.show_details()
    def fuel_type(self,fuel):
        print(f"{self_model} uses {fuel} as fuel")
        my_car=car("Honda",6,"City Rider",180)
        my_car.show_details()
        my_car.fuel_type("Petrol")
print("Is car a subclass of Vehicle?"issubclass(car,vehicle))

    