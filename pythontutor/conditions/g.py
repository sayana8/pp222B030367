a=int(input())
b=int(input())
c=int(input())
d=int(input())
if(abs(c-a)!=0 and d-b==0 or c-a==0 and abs(d-b)!=0):
    print("YES")
else:
    print("NO")