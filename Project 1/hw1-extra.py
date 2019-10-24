#Wesbert J Edouard
#U73502535
#September 13, 2019
#Fall 2019 - Data Structures and Algorithms

from file import read
newlist = read()
print(newlist)

def increasetrendpoints():
    v = (len(newlist) - 1)
    x = 0
    y = 1
    boolean = 0
    while x < v:
        if (newlist[x] - newlist[y]) < 0:
            #print("\nincreasing trend at position", x, "to", y, end=" ")
            if (y + 1) <= v:
                x = y
                y += 1
                if (newlist[x] - newlist[y]) > 0:
                    boolean += 1
                    if boolean < 2:
                        print("\ntrend change point is value: ", newlist[y], "at position: ", y)
        else:
            exit()


def decreasetrendpoints():
    v = (len(newlist) - 1)
    x = 0
    y = 1
    boolean = 0
    while x < v:
        if (newlist[x] - newlist[y]) > 0:
            print("\ndecreasing trend at position", x, "to", y, end=" "),
            print("\n", newlist[y], end=" "),
            if (y + 1) <= v:
                x = y
                y += 1
            if (newlist[x] - newlist[y]) > 0:
                boolean += 1
                if boolean < 2:
                    print("\ntrend change point is value: ", newlist[y], "at position: ", y)
        else:
            exit()


increasetrendpoints()
decreasetrendpoints()

