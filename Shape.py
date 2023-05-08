"""
This program is for calculating different
shape depending on the user's input
"""
from abc import ABCMeta, abstractmethod
class Shape:
    """Shape class for different  shape type"""
    __metaclass__=ABCMeta 
    def __init__(self,shape_type):
        """To initialize object of class Shape Input Parameters"""
        self.shape_type=shape_type
    @abstractmethod
    def area(self):
        """Abstract method for area"""
        pass
    @abstractmethod
    def perimeter(self):
        """Abstract method for perimeter"""
        pass
class Rectangle(Shape): 
    """The inherited child class of Shape"""
    def __init__(self,length,breadth):
        """To initialize object of class Rectangle """
        Shape.__init__(self,'Rectangle')
        self.length=length
        self.breadth=breadth
    def area(self):
        """To get the area of rectangle"""
        return self.length*self.breadth
    def perimeter(self):
        """To get the perimeter of rectangle"""
        return 2*(self.length+self.breadth)
class Square(Shape):
    """The inherited child class of Shape"""
    def __init__(self,side):
        """To initialize object of class Square """
        Shape.__init__(self,'Square')
        self.side=side
    def area(self):
        """To get the area of square"""
        return self.side*self.side
    def perimeter(self):
        """To get the perimeter of square"""
        return 4*self.side
class Circle(Shape):
    """The inherited child class of Shape"""
    pi=3.14
    """To initialize object of class Circle """
    def __init__(self,radius):
        Shape.__init__(self,'Circle')
        self.radius=radius
    def area(self):
        """The function is to get the area of circle"""
        return round(Circle.pi * (self.radius ** 2), 2)
    def perimeter(self):
        """To get the perimeter of circle"""
        return round(2 * Circle.pi * self.radius, 2)

shapes = {
#The dictionary of shape classes with corresponding menu numbers
    1: Rectangle,
    2: Square,
    3: Circle,
}
""" Input for different shape"""
print("Enter the shape you want to create:")
print("1. Rectangle")
print("2. Square")
print("3. Circle")
choice = int(input("Enter your choice (1-3): "))
""" take user input"""
if choice in shapes:
    """ To create and call the appropriate shape object based on the user's choice"""
    shape_class = shapes[choice]
    """get the shape class from the dictionary"""
    if shape_class == Rectangle:
        """ To take input from user for shape dimensions"""
        length = float(input("Enter length of rectangle: "))
        breadth = float(input("Enter breadth of rectangle: "))
        shape = shape_class(length, breadth)
    elif shape_class == Square:
        side = float(input("Enter the side of square: "))
        shape = shape_class(side)
    elif shape_class == Circle:
        radius = float(input("Enter the radius of circle: "))
        shape = shape_class(radius)
    """ print area and perimeter of shape"""
    print(f"Area of {shape.shape_type}: {shape.area()}")
    print(f"Perimeter of {shape.shape_type}: {shape.perimeter()}")
else:
    print("Invalid choice.Please enter a value between 1 and 3.") 

