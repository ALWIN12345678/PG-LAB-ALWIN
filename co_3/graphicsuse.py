from graphics import rectangle
from graphics import circle

print("Read values: \n Rectangle:\n")
l=int(input("Enter length"))
b=int(input("Enter breadth"))
r_area=rectangle.area(l,b)
r_perimeter=rectangle.perimeter(l,b)


print("Circle:\n")
r=int(input("Enter radius"))
area=circle.area(circle.pi,r)
perimeter=circle.perimeter(circle.pi,r)

print("Area of Rectangle:",r_area)
print("Area of Circle:",area)
print("Perimeter of Rectangle:",r_perimeter)
print("Perimeter of Circle:",perimeter)
