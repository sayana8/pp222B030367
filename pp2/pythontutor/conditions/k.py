a=int(input())
b=int(input())
c=int(input())
d=int(input())
if(abs(a-c)==1 and abs(d-b)==2 or abs(d-b)==1 and abs(c-a)==2):
    print("YES")
else:
    print("NO")