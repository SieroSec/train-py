#!/usr/bin/env python3
import re, sys, string

# myString = """    Supergod
#     Lets try it!
#     Exit();"""

# print("Hello");
# print(myString);

# result = "sIiNgle".lower();
# print(result);

# def siero(a1, b1=False):
#     print(f"a1:{a1};type:", type(a1))
#     print(f"b1:{b1};type:", type(b1))
    
    
#     return True;

# output = siero("blahblah");
# print (output)

class Car:
    """
    Docstring describe the shit here
    """
    
    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires

    def describe(self):
        print(f"Car with an {self.engine} and tires: {self.tires}")

    def wheel_circumference(self):
        try:
            if len(self.tires) > 0:
                return self.tires[0].circumference()
            else:
                return 0
        except TypeError as error:
            print(f"Type error: {error}")
            

class Tire:
    def __init__(self, tire_type, width, ratio, diameter, brand='', construction='R'):
        self.tire_type = tire_type;
        self.width = width;
        self.ratio = ratio;
        self.diameter = diameter;
        self.brand = brand;
        self.construction = construction;
        
    def __repr__(self):
        return(f"{self.tire_type} {self.width}/{self.ratio}{self.construction}{self.diameter}")

    def circumference(self):
        """
        The cirsumference of the tire in inches.
        
        >>> tire = Tire('P', 205, 65, 15)
        >>> tire.circumference()
        80.1
        """
        side_wall_inches = (self.width * (self.ratio / 100) / 25.4)
        total_diameter = side_wall_inches * 2 + self.diameter
        return round(total_diameter * 3.14, 1)
    
        
# # from hello import Car,Tires
# tire = Tire('P', 205, 55, 15)
# myTires = [tire, tire, tire, tire]
# myCar = Car(tires=myTires, engine='V4-petrol')

# myCar.describe()
# #print(hasattr(myCar, 'tires'))
# myCar.wheel_circumference()

