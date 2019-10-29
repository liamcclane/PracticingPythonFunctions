# # Python stuffssss

# # 1. TASK: print "Hello World"
# print( "Hello World")


# # 2. print "Hello Noelle!" with the name in a variable
# name = "Noelle"
# print( "a. Hello,", name )	# with a comma
# print( "b. Hello, " + name )	# with a +


# # 3. print "Hello 42!" with the number in a variable
# name1 = 42
# print( "a. Hello,", name1 )	# with a comma
# print( "b. Hello, " + name1 )	# with a +	-- this one should give us an error!
# # Error message for Hello (b), because with the plus sign is is a string concation where name is saved as an inter type
# #         Traceback (most recent call last):
# #         File "c:\Users\lia_m\Documents\theDojo\python_stack\python\fundaments\hello_world.py", line 16, in <module>
# #         print( "b. Hello, " + name )	# with a +	-- this one should give us an error!
# #         TypeError: can only concatenate str (not "int") to str


# # 3a. Store your favorite number in a variable, and then use it to print the string 
#     # “Hello {{num}}!” using a comma in the print function (#3a)
# favNum = 2.718
# print("Hello, ", favNum) # error, can br fixed with srt(favNum)
# print("Hello,", str(favNum)) # then you can take the space away since string concat now works 


# # 3b. Store your favorite number in a variable, and then use it to print the string 
#    # “Hello {{num}}!” using a + in the print function (#3b)
# favNum2 = 3.14159
# print("Hello, " + favNum2) # error, can br fixed with srt(favNum)
# print("Hello, " + str(favNum2)) # then you can take the space away since string concat now works 


# # 4. print "I love to eat sushi and pizza." with the foods in variables
# fave_food1 = "sushi"
# fave_food2 = "pizza"
# print( "a. My two favotie foods are {} and {}." .format(fave_food1,fave_food2)) # with .format()
# print( f"b. My two favotie foods are {fave_food1} and {fave_food2}." ) # with f string

