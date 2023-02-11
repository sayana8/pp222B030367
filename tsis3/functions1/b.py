#2  =
n=float(input("Enter temperature in Fahrenheit "))
def fromftoc(n):
    c=float((5/9)*(n-32))
    print(c, "C")
    print(n, 'F is equal to ' , round(c,3), 'C.')
fromftoc(n) 