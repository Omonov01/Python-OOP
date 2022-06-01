from main import Car

class Bus(Car):
    """" Class for buss """
    def __init__(self, colour, cost, make_year, km,in_person,manufacturer):
        """" value of Buss """
        super().__init__(colour, cost, make_year, km)
        
        self.in_person = in_person
        self.oil = 5
        self.manufacturer = manufacturer
    
    def get_in_person(self):
        """" get person number """
        return self.in_person
    
    def get_info(self):
        info = f'{self.colour} {self.cost} {self.make_year} {self.km} {self.in_person}'
        return info
        
# bus = Bus('Yellow',15000,2003,20,50)
# print(f'{bus.get_age_of_car(2022)} In person {bus.get_in_person()}')
# print(bus.get_info())
class Manufacture():
    def __init__(self,firm,brend):
        
        self.firm = firm
        self.brend = brend
        
    def get_manufacturer(self):
        return f'{self.firm} {self.brend}'
    
manufacturer = Manufacture('Toyota','Nissan')
bus = Bus('Black',20000,2005,15,60,manufacturer)
    
print(f'{bus.get_info()} was made {bus.manufacturer.get_manufacturer()}')