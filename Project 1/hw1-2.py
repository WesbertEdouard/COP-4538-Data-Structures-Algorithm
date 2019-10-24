#Wesbert J Edouard
#U73502535
#September 13, 2019
#Fall 2019 - Data Structures and Algorithms

from file import read
numbers = read()
print("The File array:")
print(numbers)
mid_point = int(len(numbers) / 2)


def reverse():
    temp = 0
    x = 0
    y = (len(numbers) - 1)
    for x in range(x, y):
        if x < mid_point:
            temp = numbers[x]
            numbers[x] = numbers[y]
            numbers[y] = temp
            y -= 1
    print(numbers)


def minmax():

    y = len(numbers)
    varMax = 0
    for x in range(0, y):
        if varMax < numbers[x]:
            varMax = numbers[x]
    varMin = varMax
    for x in range(0, y):
        if varMin > numbers[x]:
            varMin = numbers[x]
    print("\nMaximum Number:", varMax)
    print("Minimum Number:", varMin)


print("\nThe Reverted array:")
reverse()
minmax()


