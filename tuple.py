#Accessing items in a tuple

my_tuple = (10,30,40,'a','b')
print(my_tuple[3])

#Adding items to tuple

my_tuple = ("Rwanda","Kenya")
list1 = list(my_tuple)
list1.append("Tanzania")
list1=tuple(list1)
print(list1)

#Removing items from tuple
my_tuple = ("Rwanda","Kenya","Tanzania")
my_list = list(my_tuple)
my_list.remove("Rwanda")
my_list=tuple(my_list)
print(my_list)