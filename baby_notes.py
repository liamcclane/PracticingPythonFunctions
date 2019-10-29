# # More Basic Python Notes

# # for sting example
# x = 10
# if x > 50:
#     print("bigger than 50")
# else:
#     print("smaller than 50")

# # example of pass
# class EmptyClass:
#     pass
# my_string = [5,6,8]
# for val in my_string:
#     pass

# # examples of data types

# # Tuples- are IMMUTABLE (not mutatable) can NOT be over written once declared
# dog = ('Bruce', 'cocker spaniel', 19, False)
# print(dog[0])		# output: Bruce
# # dog[1] = 'dachshund'	# ERROR: cannot be modified ('tuple' object does not support item assignment)

# # Lists- a mutatable data set that can hold a group of values
# empty_list = []
# ninjas = ['Rozen', 'KB', 'Oliver']
# print(ninjas[2]) 	# output: Oliver
# ninjas[0] = 'Francis'
# ninjas.append('Michael')
# print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
# ninjas.pop()
# print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
# ninjas.pop(1)
# print(ninjas)	# output: ['Francis', 'Oliver']

# # Dictionaries- a group of key-value pairs: Key->'name' Value->"Oliver"
# empty_dict = {}
# new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
# new_person['name'] = 'Jack'	# updates if the key exists
# new_person['hobbies'] = ['climbing', 'coding']	# adds a key-value pair if the key doesn't exist
# print(new_person)	
# # output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
# w = new_person.pop('weight')	# removes the specified key and returns the value
# print(w)		# output: 160.2
# print(new_person)	
# # output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}


# # For loops

# #  in a list
# my_list = ["abc", 123, "xyz"]
# for i in range(0, len(my_list)):
#     print(i, my_list[i])
# # output: 0 abc, 1 123, 2 xyz
# for v in my_list:
#     print(v)
# # output: abc, 123, xyz

# # in a dictonary
# my_dict = { "name": "Noelle", "language": "Python" }
# for k in my_dict:
#     print(k)
# output: name, language: which are the key codes, not the values.... interesting
# if we want the values inside the dictonary and not the key codes the loop would look like this
# for k in my_dict:
#     print(my_dict[k])
# output: Noelle, Python
# another way to iterate through the keys
# for key in my_dict.keys():
#     print(key)
# to iterate through the values
# for val in my_dict.values():
#     print(val)
# #to iterate through both keys and values
# for key, val in my_dict.items():
#     print(key, " = ", val)


# # While loops
# count = 0
# while count < 5:
#     print("looping -", count)
#     count += 1

# # While/Else loop!!!
# y = 3
# while y > 0:
#     print(y)
#     y = y - 1
# else:
#     print("Final else statement")

# # Functions, example
# def add(a,b):	# function name: 'add', parameters: a and b
#     x = a + b	# process
#     return x	# return value: x
# new_val = add(3, 5)    # calling the add function, with arguments 3 and 5
# print(new_val)    # the result of the add function gets sent back to and saved into new_val, so we will see 8
# # another example
# def say_hi(name):
#     print("Hi, " + name)
# # invoking the function 3 times, passing in one argument each time
# say_hi('Michael')
# say_hi('Anna')
# say_hi('Eli')
# # ARGUMETNS vs PARAMETERS
# # above, the arguments are 'Micheal', 'Anna', and 'Eli'
# # while the parameter is the variable name


