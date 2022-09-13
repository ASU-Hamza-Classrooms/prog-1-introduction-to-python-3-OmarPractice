#!/bin/python3

#Add the following functions:
#
#reverseStr - takes as input a string and returns the reverse of it
def reverseStr(str):   #takes as input a string and returns the reverse of it
    return str[::-1]


#containsWord - takes as input two strings, containingStr and containedStr,
#and returns "Yes" if containedStr is anywhere within containingStr 
#and returns "No" otherwise
def containsWord(containingStr, containedStr):
    if containedStr in containingStr:
        x = ("Yes")
    else:
        x = ("No")
    return x
#isPalindrome - takes as input a string and returns "Yes" if it is
#palindrome and "No" otherwise  
def isPalindrome(str):
    revStr = reverseStr(str)
    if str == revStr:
        x = ("Yes")
    else:
        x = ("No")
    return x
#upperCaseStr - takes as input a string and returns the identical string
#with the characters 'a' ... 'z' changed to uppercase
#
def upperCaseStr(Str):
    return Str.upper()
