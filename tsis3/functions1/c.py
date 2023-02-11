#3  =
numheads=int(input("Enter the number of heads: "))
numlegs=int(input("Enter the number of legs: "))
def solve(numheads, numlegs):
    c=int(((4*numheads-numlegs)/2))
    r=int(numheads-c)
    print("Rabbit: " , r ,"\n"  'Chiken: ' , c)

solve(numheads, numlegs)
    