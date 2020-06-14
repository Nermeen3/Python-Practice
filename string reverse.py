
# printing the reverse of a string using recursion

def printReverse(string, lastElement):
    if lastElement == -1:
        return
    print(string[lastElement])
    printReverse(string, lastElement-1)

string = 'Hello Friends!'
printReverse(string, len(string)-1)


print()
# reversing a string by modifying the input string itelsf
# without allocating extra space for a new array/string

def ReverseString(string, head, tail):
    if head > tail:
        return string
    temp = string[head]
    string[head] = string[tail]
    string[tail] = temp
    return ReverseString(string, head+1, tail-1)

string2 = ["H","e","l","l","o", "o"]
head, tail = string2[0], string2[len(string2)-1]
print(head, tail)
print(ReverseString(list(string2), 0, len(string2)-1))
