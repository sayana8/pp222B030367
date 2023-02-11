#8  =
a = [int(i) for i in input().split()]
a.append(" ")
def spy_game(a):
    for i in range(0,len(a)):
        if a[i] == 0:
            for x in range(i+1,len(a)):
                if a[x] == 0:
                    for y in range(x+1,len(a)):
                        if a[y] == 7:
                            print("true")
                            return True 
    print("false")
spy_game(a)

"""a = [int(i) for i in input().split()]
for x in range(len(a)):
    if(a[x] != 0 or a[x]!=7):
        a.remove(a[x])
if (a[0])=="0" and a[1]==0 and a[2]==1:
    print("yes")
else:
    print("no")"""

