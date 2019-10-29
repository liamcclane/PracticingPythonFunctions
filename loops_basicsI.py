# # Basic loops assignment

# # 1 Basic - Print all integers from 0 to 150.
# # using a for loop
# for i in range(151):
#     print(i)
# # using a while loop going up
# upperBound = 150
# count = 0
# while count < upperBound + 1:
#     print(count)
#     count += 1
# # using a while loop going down
# while upperBound > -1:
#     print(upperBound)
#     upperBound -= 1

# # 2 Multiples of Five - Print all the multiples of 5 from 5 to 1,000
# # using a for loop
# for i in range(5,1001,5):
#     print(i)
# for i in range(1,201):
#     print(i * 5)
# for i in range(200):
#     i +=1
#     i *=5
#     print(i)
# # see above for the last loop, we can do what ever you want to i in the side the loop 
# # BUT at the end of the loop when it wants to start the count over, it will reset to 
# # it's orginal number from the begining of the loop
# # while loop THAT DOES NOT WORK
# # while loops have declaration outside, thus changing the inside count
# while count < 201:
#     count += 1
#     count *=5
#     print(count)
# # but this while loop will work
# count = 0
# while count < 201:
#     print(count * 5)
#     count += 1


# # 3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, 
# # print "Coding" instead. If divisible by 10, print "Coding Dojo".
# for i in range(1,101):
#     if i%5==0:
#         print( i,  "Coding ", end='')
#         if i%10==0:
#             print("Dojo")
#         print('') # slightly weird indentation...
# for i in range(1,101):
#     if i%10==0:
#         print( i, 'Coding Dojo')
#     elif i%5==0:
#         print(i, 'Coding')


# # 4 Whoa. That Sucker's Huge - Add odd integers from 
# # 0 to 500,000, and print the final sum.
# sum = 0
# for i in range(1,500000,2):
#     sum = sum + i
# print("the final sum is", sum)


# # 5 Countdown by Fours - 
# # Print positive numbers starting at 2018, counting down by fours.
# # as for loop
# for i in range(2018, -1, -4):
#     print(i)
# # as a while loop
# countDown = 2018
# while countDown > -1:
#     print('countDown')
#     countDown = countDown -4


# # 6 Flexible Counter
# #   Set three variables: lowNum, highNum, mult. 
# #   Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. 
# #   For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
# lowNum = 2
# highNum = 9
# mult = 3
# for i in range(lowNum, highNum+1):
#     if i%mult == 0:
#         print(i, '' , end= '')
# # again in another for loop
# # this one below does NOT work because it assumes that the first low number is a mulitple multip which isn't always the case
# for i in range(lowNum, highNum, mult):
#     print(i, '', end = '')

