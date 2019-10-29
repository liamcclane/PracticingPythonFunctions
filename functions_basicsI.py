# # Functions BasicsI
# # Predict the output
# #1
# def a():
#     return 5
# print(a()) # output:5

# #2
# def a2():
#     return 5
# print(a2()+a2()) # output: 10

# #3
# def a3():
#     return 5
#     return 10
# print(a3()) # output:5

# #4
# def a4():
#     return 5
#     print(10)
# print(a4()) # output:5 # note that it will not print 10 becuse it comes after the return statement

# #5
# def a5():
#     print(5)
# x = a5()
# print(x) # output: 5 none # note that the function does not have a return statement

# #6
# def a6(b,c):
#     print(b+c)
# print(a6(1,2) + a6(2,3)) # output: 3(enter)5(enter)error 
# # again note that a6() has no return AND we are trying to string concat

# #7
# def a7(b,c):
#     return str(b)+str(c)
# print(a7(2,5)) # output: 25 
# # becuase the numbers, or parameters being passed into the function become strings without a space between them

# #8
# def a8():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(a8()) # output: 100 (enter)10
# # since this function does not have any parameters it will always print 100 and return 10 when called

# #9
# def a9(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a9(2,3)) # output: 7
# print(a9(5,3)) # output: 14
# print(a9(2,3) + a9(5,3)) # output: 21
# # note that for the last print statement we get 'math' being done becuase they are both intergers
# # if ran print(str(a9(2,3)) + a9(5,3)) # output: error # we will get an errro message of diff types 
# # if ran print(str(a9(2,3)) + str(a9(5,3))) # output: 714 # these numbers as a string

# #10
# def a10(b,c):
#     return b+c
#     return 10
# print(a10(3,5)) # output: 8

# #11
# b = 500
# print(b)
# def a11():
#     b = 300
#     print(b)
# print(b)
# a11()
# print(b)
# # output: 500 500 300 500
# # NOTE the function is scope specific line 77,81,83 all refer to the b on 76
# # while print on 80 is the b declared on line 79...... remember that
# # variables in python are score specific

# #12
# b = 500
# print(b)
# def a12():
#     b = 300
#     print(b)
#     return b
# print(b)
# a12()
# print(b)
# # output: 500 500 300 500
# # the only difference between problems 11 and 12 is that a12() is now returning something 
# # and can be stored at another variable

# #13
# b = 500
# print(b)
# def a13():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=a13()
# print(b) # output: 500 500 300 300
# # on line 111 we can see b from line 104 is being over written and set to 300
# # which will happen anytime a13() is called since there are no parameters or argumets to augment the return

# #14
# def a14():
#     print(1)
#     b14()
#     print(2)
# def b14():
#     print(3)
# a14() # output: 1 3 2
# # reading this line for line, we start at 123-> 117,118,119 ->121,122 ->120 ->end of 123

# #15
# def a15():
#     print(1)
#     x = b15()
#     print(x)
#     return 10
# def b15():
#     print(3)
#     return 5
# y = a15()
# print(y) #outputing:1 3 5 10
