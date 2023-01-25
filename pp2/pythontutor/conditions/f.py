a=int(input())
b=int(input())
c=int(input())
if(a!=b and a!=c and b!=c):
    print("0")
elif(a==b and a==c and b==c):
    print("3")
else:
    print("2")