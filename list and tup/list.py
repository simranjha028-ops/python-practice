#Movie list operations
movies = ["Interstellar","Inception","Shutter island","Harry potter"]
print(movies)
print(type(movies))

#add a movie
movies.append("Charlie")
print(movies)

#remove a movie
movies.remove("Inception")
print(movies)

#replace
movies[2] = ("Bruce lee")
print(movies)

#reverse
print(movies[::-1])

#expected output
#['Interstellar', 'Inception', 'Shutter island', 'Harry potter']
#<class 'list'>
#['Interstellar', 'Inception', 'Shutter island', 'Harry potter', 'Charlie']
#['Interstellar', 'Shutter island', 'Harry potter', 'Charlie']
#['Interstellar', 'Shutter island', 'Bruce lee', 'Charlie']
#['Charlie', 'Bruce lee', 'Shutter island', 'Interstellar']


#Number list operations
num = [2,34,5,6,32,45,78,90]
print("Maximum:",max(num))
print("Minimum:",min(num))
print("Sum:",sum(num))

#expected output
#Maximum: 90
#Minimum: 2
#Sum: 292




#List copy check
#create list,copy it,and modify copied list

list = ["Apple","Banana","Grapes","Pear"]
list_copy = (list.copy())
list_copy.append("Berries")
print("Old list:",list)
print("New list:",list_copy)

#expected output
#Old list: ['Apple', 'Banana', 'Grapes', 'Pear']
#New list: ['Apple', 'Banana', 'Grapes', 'Pear', 'Berries']


#student list operations
#create student list,add,remove,count, and sort the list

stud_list = ["Simran","Sakshi","Sneha","Namrata","Simran"]
print("The Original list of students are:",stud_list)
stud_list.append("Rutuja")
print(stud_list)
stud_list.remove("Simran")
print(stud_list)
print(stud_list.count("Simran"))
stud_list.sort()
print(stud_list)

#expected output
#The Original list of students are: ['Simran', 'Sakshi', 'Sneha', 'Namrata', 'Simran']
#['Simran', 'Sakshi', 'Sneha', 'Namrata', 'Simran', 'Rutuja']
#['Sakshi', 'Sneha', 'Namrata', 'Simran', 'Rutuja']
#1
#['Namrata', 'Rutuja', 'Sakshi', 'Simran', 'Sneha']