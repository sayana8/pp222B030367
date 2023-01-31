#Set items are unchangeable, but you can remove items and add new items.

thisset = {"apple", "banana", "cherry"}
print(thisset) 

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)    #duplicate valiues will be ignored 

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#String, int and boolean data types:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}


thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#add
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")  #orange, apple, banana, cherry 


print(thisset) 



thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)  #cherry, banana, apple, pineapple, mango, papapya

print(thisset)




thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)



