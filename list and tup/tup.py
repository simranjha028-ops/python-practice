#tuple indexing
#create a tuple,print 1st el,last el,middle el,and try  modifying

tup = (2,34,21,3,4,56,78)
print(type(tup))
print("The first element is:",tup[0])
print("The last element is:",tup[6])
print("The middle element is:",tup[3])


#expected output
#<class 'tuple'>
#The first element is: 2
#The last element is: 78
#The middle element is: 3
#tuples dont allow modification as it is immutable


#diff in list and tuple
#create a list and tuple with same value,modify list and observe tuple

list = [23,45,33,56]
print("The old list is:",list)
tup = (23,45,33,56)
list[2] = 68
print("The new list is:",list)
#expected output
#The old list is: [23, 45, 33, 56]
#The new list is: [23, 45, 68, 56]



#modify tup
tup(0) = 9
print(tup)
#here , error occurs as tuples are immutable