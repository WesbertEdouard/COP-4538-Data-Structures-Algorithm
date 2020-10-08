def readFile():
    fToRead = open("array2.txt", "r")
    myList = []
    for lineIt in fToRead:
        myList = lineIt.split(" ")
        '''print(myList)'''
    return myList