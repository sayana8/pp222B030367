#change list items

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) #apple, black.., cherry

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)   #apple, bkack..., watr, orange...


thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)   #apple, black, water...

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) #apple, watermtlon.


thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)  #apple, banana, water, cherry 