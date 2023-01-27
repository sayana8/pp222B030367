a=int(input())
b=int(input())
c=int(input())
d=int(input())
if(a==c and abs(d-b)>0 or abs(a-c)>0 and b==d or abs(a-c)==abs(d-b)):
    print("YES")
else:
    print("NO")