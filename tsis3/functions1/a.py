#1   =
#from grams to ounces
n=float(input("Enter the gram amount  "))
def gramintoounces(n):
    print( n, 'gram is ',  n*28.3495231, 'ounes.' )
    print("approximately, it is " , round(n*28.3495231, 3), ' ounces')
gramintoounces(n)


""" 
from ounces to grams
n=float(input("Enter the ounce amount  "))
def ouncesintograms(n):
    print( n, 'ounce is ',  n/28.3495231, 'gram.' )
    print("approximately, it is " , round(n*28.3495231, 3), ' gram')
ouncesintograms(n) 
"""