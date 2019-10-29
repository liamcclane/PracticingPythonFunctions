# Functions BasicsII / Lia McClane

# 1 Biggie Size - 
# Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, 
# but whose values are now [-1, "big", "big", -5]
def biggie_size(array):
    for i in range(len(arr,ay)):
        if array[i]>0:
            array[i]='big'
    return array
print(biggie_size([0,-5,-6,8,9,10]))


# 2 Count Positives - 
# Given a list of numbers, create a function to replace the last value with the number 
# of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(array):
    count = 0
    for val in array:
        if val > 0:
            count += 1
    array[len(array)-1] = count
    return array
print([-5,-9,0,32,-6,22])
print(count_positives([-5,-9,0,32,-6,22]))


# 3 Sum Total - 
# Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sum_total(array):
    sum = 0
    for val in array:
        sum += val
    return sum
print(sum_total([1,1,1,1]))
print(sum_total([1,1,1,55]))


# 4 Average - 
# Create a function that takes a list and 
# returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5
def avg(list):
    sum = 0
    for val in list:
        sum += val
    return (sum/len(list))
print(avg([5,5,5,6]))

# 5 Length - 
# Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def lengthFun(array):
    return len(array)
print(lengthFun([1,1,1,1,1,4]))
print(lengthFun([1,1]))

# 6 Minimum - 
# Create a function that takes a list of numbers and returns the minimum value in the list. 
# If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minFun(array):
    if len(array)<0:
        return False
    minInt = array[0]
    for val in array:
        if val<minInt:
            minInt = val
    return minInt
print(minFun([600,80,99,26,3,5]))

# 8 Ultimate Analysis - 
# Create a function that takes a list and returns a dictionary that has the 
# sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) 
# should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(array):
    myDictonary = {'sumTotal': 0, 'average': 0, 'minimum': array[0], 'maximun': array[0], 'length': len(array)}
    for val in array:
        if myDictonary['minimum']<val:
            myDictonary['minimum'] = val
        if myDictonary['maximun']>val:
            myDictonary['maximun'] = val
        myDictonary['sumTotal']+= val
        myDictonary['average']=myDictonary['sumTotal']/len(array)
    return myDictonary
print(ultimate_analysis([1,2,1,2,4,0]))
print(ultimate_analysis([1,0]))
print(ultimate_analysis([15,4,1,0]))


# 9 Reverse List - 
# Create a function that takes a list and 
# return that list with values reversed. Do this without creating a second list. 
# (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(array):
    for i in range(0, (len(array)-1)//2):
        temp = array[i]
        array[i] = array[len(array)-1-i]
        array[len(array)-1-i] = temp
    return array
print(reverse_list([11,12,13]))
print(reverse_list([11,12,13,14,15,16]))
print(reverse_list([11,12,13,14,15,16,18]))


