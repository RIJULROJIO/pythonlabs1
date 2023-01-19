class Rectangle():
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length + self.breadth)

l1=float(input("Enter the length of the rectangle:"))
b1=float(input("Enter the breadth of the rectangle:"))
l2=float(input("Enter the length of the rectangle:"))
b2=float(input("Enter the breadth of the rectangle:"))
rect1=Rectangle(l1,b1)
rect2=Rectangle(l2,b2)
print("Area of rectangle 1 is{} and perimeter is{}:".format(rect1.area(),rect1.perimeter()))
print("Area of rectangle 2 is{} and perimeter is{}:".format(rect2.area(),rect2.perimeter()))
print(rect1.area()>rect2.area())