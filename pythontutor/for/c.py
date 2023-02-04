a=int(input())
b=int(input())
if(a%2==1):
    for i in range(a, b-1, -2):
        print(i) 
else:
    a-=1
    for i in range(a, b-1, -2):
        print(i) 