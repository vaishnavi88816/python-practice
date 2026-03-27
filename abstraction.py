from abc import ABC,abstractmethod
import math
class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass 
    
    @abstractmethod
    def area(self):
        pass
    
class square(abstract):
    def __init__(self,side):
        self.side=side
        
    def perimeter(self):
        return 4*self.side
    
    def area(self):
        return self.side * self.side
        
        
class circle(abstract):
    def __init__(self,radius):
        self.radius=radius
    def perimeter(self):
        return 2 * math.pi * self.radius
        
    def area(self):
        return  math.pi*self.radius * self.radius
obj = circle(7)
obj2 = square(12)
print("circle perimeter:-",obj.perimeter())
print("circle area:-",obj.area())
print("square perimeter:-",obj2.perimeter())
print("square area:-",obj2.area())