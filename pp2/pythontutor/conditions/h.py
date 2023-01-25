a=int(input())
b=int(input())
c=int(input())
d=int(input())
if(abs(c-a)==1 and d-b==0 or abs(d-b)==1 and a-c==0 or abs(a-c)==1 and abs(d-b)==1):
    print("YES")
else:
    print("NO")