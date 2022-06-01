class Car:
    car_num = 0
    def __init__(self,colour,cost,make_year,km):
        """" class about car """
        self.colour = colour
        self.cost = cost
        self.make_year = make_year
        self.km = km
        Car.car_num += 1
    
    def get_info(self):
        """" get full information about car """
        return f'{self.colour} {self.cost} {self.make_year} {self.km}'
    
    def get_colour(self):
        """" get car colour """
        return f'Our car colour is {self.colour}'
    
    def get_cost(self):
        """" get car cost """
        return f'Our car cost is {self.cost}'
    
    def get_makeyear(self):
        """" get car manufacturer year """
        return f'Our car data of manufacture {self.make_year}'
    
    def get_km(self):
        """" get car's moving distance """
        return f'Our car moving distance is {self.km}'
        
    def get_age_of_car(self,yil):
        """" get car's age """
        return f'Our car age {yil - self.make_year}'
        
    @classmethod
    def get_class(cls):
        return cls.car_num

class Carpark():
    def __init__(self,name):
        """" get information about Carpark """
        self.name = name
        self.number = 0
        self.information = []
        
    def add_car(self,car):
        """" append car object to self.information list """
        self.information.append(car)
        self.number += 1
        
    def get_data(self):
        """" get information about carpark """
        return f"Our carpark has {self.number}"
    
    def get_avtoname(self):
        """" get informatinon about car which inside carpark """
        return [info.get_info() for info in self.information ]
     
    
car1 = Car('BLACK',20000,1995,200)
car2 = Car('wHITE',25000,2003,25)
car3 = Car('Yellow',15000,2004,200)
car4 = Car('Yellow',15000,2004,200)
car5 = Car('Yellow',15000,2004,200)
list = [car1,car2,car3,car4,car5]

carpark = Carpark('speed')

for car in list:
    carpark.add_car(car)

print(car2.get_class())
print(carpark.get_data())
print(carpark.get_avtoname())
