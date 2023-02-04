s = input()
a = s[:s.find('h')] 
b = s[s.find('h'):s.rfind('h') + 1]
c = s[s.rfind('h') + 1:]
s = a + b[::-1] + c
print(s)

#In the hole in the ground there lived a hobbit
#In th a devil ereht dnuorg eht ni eloh ehobbit