""" Program to print area of geometrical shapes-triangle,
rectangle and circle using function"""

pi=3.14
r=5
base=10
per=5

def area_circle():
    area= pi*r*r
    print("Area of circle is ",area)

def area_ra_triangle():
    area=0.5*base*per
    print("Area of triangle is ",area)

def area_rectangle():
    area=base*per
    print("Area of rectangle is ",area)

area_circle()
area_ra_triangle()
area_rectangle()
