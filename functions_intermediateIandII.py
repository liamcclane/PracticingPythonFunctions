# Function Intermediate I/ Lia McClane
import random
def randInt(min = 0,max = 100):
    if max<0:
        print('sorry we need a max number greater than 0')
    elif min > max:
        print('sorry please give a max greater than the min')
    else: 
        if max != 100 and min != 0:
            return round(random.random()*(max-min)+min)
        if min != 0:
            return round(random.random()*(100-min)+min)
        if max != 100:
            return round(random.random()*max)
    return round(random.random()*100)
print(f"This function call should always return a random number between 0 and 100 randInt() = {randInt()}")
print(f"This function call should always return a random number between 0 and 10 randInt(max = 10) = {randInt(max = 10)}")
print(f"This function call should always return a random number between 98 and 100, randInt(min = 98) = {randInt(min = 98)}")
print(f"This function call should always return a random number between 22 and 25 randInt(min = 22, max = 25) = {randInt(min = 22, max = 25)}")
print(f"This function call takes into account the edge case of min>max, randInt(min = 7, max = 2) {randInt(min = 7, max = 2)}")
print(f"This function call takes into account the edge case of 0<max, randInt(max = -5) {randInt(max = -5)}")






# Intermediate Functions II
# 1 Update values in the given dictonary and a list

# 1a Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x = [ [5,2,3], [10,8,9] ]
x[1][0]=15
print(f"x was orginally [ [5,2,3], [10,8,9] ]  and is now {x}")
# 1a another way to chage the occurance of 10 the list [ [7,8,99,10],[0,2,-6,10,10] ] is
x2 = [[7,8,99,10], [0,2,-6,10,10]]
for val in x2:
    for i in range(len(val)):
        if 10 == val[i]:
            savedIndex = i
            val[savedIndex] = 15
print(f"x2 was orginally [ [7,8,99,10],[0,2,-6,10,10] ] and is now {x2}")


# 1b Change the last_name of the first student from 'Jordan' to 'Bryant'
# hard coding
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print("student 1's orginal information was {'first_name':  'Michael', 'last_name' : 'Jordan'}")
print("student 1's new information is {student[0]}")


# 1c In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
# hard coding it
sports_directory['soccer'][0] = 'Andres'
print("sports_directory key code 'soccer' used to say ['Messi', 'Ronaldo', 'Rooney'] ")
print('now has changed to')
for i in range(len(sports_directory['soccer'])):
    print(f"{sports_directory['soccer'][i]} and ")
# iterating though looking for 'Messi' and chaning all occurances to 'Andres'
sports_directory2 = {
    'american_football' : ['Peyton', 'Eli'],
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
for i in range(len(sports_directory2['soccer'])):
    if 'Messi' in sports_directory2['soccer']:
        sports_directory2['soccer'][i] = 'Andres'
print("my new sports_directory2 changed from 'soccer' : ['Messi', 'Ronaldo', 'Rooney']  to")
for i in range(len(sports_directory2['soccer'])):
    print(f"{sports_directory2['soccer'][i]} and ")


# 1d Change the value 20 in z to 30
z = [{'x': 10, 'y': 20}] # this is a list with on dictonary inside
# hard coding it
z[0]['y'] = 30
print("z used to look like [{'x': 10, 'y': 20}] now {z}")


# 2 Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops 
# through each dictionary in the list and prints each key and the associated value. 
# For example, given the following list:
students2 = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
def iterateDictionarycopy(anyList):
    stringReturn = ''
    for val in anyList:
        stringReturn += f"first_name - {val['first_name']}, last_name - {val['last_name']}\n"
    return stringReturn
print(iterateDictionarycopy(students2))


# 3 Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, 
# the function prints the value stored in that key for each dictionary. 
# For example, iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB
def iterateDictionary2(key_name, some_list):
    stringReturn = ''
    for val in some_list:
        stringReturn += f"{val[key_name]} \n"
    return stringReturn
print(iterateDictionary2('last_name',students2))


# 4 Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key 
# along with the size of its list, and then prints the associated values within each key's list. For example:
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printDictonaryInfo(my_dictonary):
    # outputStr = ''
    for key in my_dictonary:
        print(f"{len(my_dictonary[key])} {key.upper()}")
        for val in my_dictonary[key]:
            print(val)
        print("")
printDictonaryInfo(dojo)
# old one.....
# def printDictonaryInfo(my_dictonary,arr_of_keys):
#     outputStr = ''
#     for val in arr_of_keys:
#         outputStr += f"{len(my_dictonary[val])} {val.upper()}\n"
#         for val2 in my_dictonary[val]:
#             outputStr += f"{val2}\n"
#         outputStr += '\n'
#     return outputStr
# print(printDictonaryInfo(dojo,['locations', 'instructors']))











# # 1b again in a different way
# # looking for all the students whos last name is Jordan, then printing out all their names
# students1 = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'},
#     {'first_name' : 'Michealla', 'last_name' : 'Jordan'},
#     {'first_name' : 'Joshua', 'last_name' : 'Rosales'},
#     {'first_name':  'Joey', 'last_name' : 'Jordan'},
#     {'first_name':  'Jessica', 'last_name' : 'Jordan'},
# ]

# # I have created a new list of indexes all the students from student1 who's last names are Jordan
# list_of_Jordans = []
# for val in students1:
#     for i in range(len(students1)):
#         if val['last_name'] == 'Jordan':
#             list_of_Jordans.append(i)
# print(list_of_Jordans)


# # lets' out put that 
# print('')
# print('these are all the students who have the last name Jordan:')
# for val in list_of_Jordans:
#     print(students1[val]['first_name']+ ' '+ students1[val]['last_name'])
# # then chaing Michal Jordan's last name to Bryant
# for val in list_of_Jordans:
#     if students1[val]['first_name'] == 'Micheal':
#         students1[val]['last_name'] = 'Bryant'
# print('Now we changed just Michal Jordan to Micheal Bryant')
# for val in list_of_Jordans:
#     print(students1[val]['first_name']+ ' '+ students1[val]['last_name'])
