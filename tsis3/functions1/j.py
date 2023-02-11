#9      =
#volum eof the sphere 
from math import *
import math
r=float(input("Enter the radius of the sphere : "))
def volume(r):
    print("Volume of the sphere is : ", round((4/3)* math.pi * r*r*r , 4) )
volume(r)