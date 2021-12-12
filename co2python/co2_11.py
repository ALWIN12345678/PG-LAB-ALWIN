#lambda function to find area of square,rectangle and triangle

s_area=lambda a:a*a
r_area=lambda a,b:a*b
t_area=lambda b,h:1/2*b*h
print("Area of square:",s_area(10))
print("Area of rectangle",r_area(10,20))
print("Area of triangle:",t_area(5,3))