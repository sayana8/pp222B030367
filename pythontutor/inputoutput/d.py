t=int(input())
if(t>=1440):
    t-=t//1440*1440
print(t//60)
print(t%60)