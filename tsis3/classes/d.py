#4
class Point:
    global mass
    mass = []
    print('Enter the cordinates: ')
    for i in range(4):
        print('x1: ', end = '') if i == 0  else print('y1: ', end = '') if i == 1 else print('x2: ', end = '')  if i == 2 else print('y2: ', end = '')
        mass.append(int(input()))
        

    def __init__(self):
        self.x1, self.y1, self.x2, self.y2 = mass[0],mass[1],mass[2], mass[3]

    def show(self):
        print(self.x1, self.y1, self.x2, self.y2)

    def dist(self):
        print(((self.x2 - self.x1)**2 + (self.y2 -self.y1 )**2)**0.5)

    def move(self):
        print('Enter other cordinates:')
        mass1 = []
        for i in range(4):
            print('x1: ', end = '') if i == 0  else print('y1: ', end = '') if i == 1 else print('x2: ', end = '')  if i == 2 else print('y1: ', end = '')
            mass1.append(int(input()))
        mass[0], mass[1], mass[2], mass[3] =  mass1[0],mass1[1],mass1[2], mass1[3]
    
Point()
display = ''
while display != '4':
    display = input("Enter the command:  ")
    if display == 'show':Point().show()
    elif display == 'move':Point().move()
    elif display == 'dist':Point().dist()
    elif display == 'exit':exit()