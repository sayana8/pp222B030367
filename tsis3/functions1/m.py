#12     =
a = [int(i) for i in input().split()]
def histogram(a):
    for x in range(len(a)):
        print("*"*a[x], end=' ')
        print()
histogram(a) 
    