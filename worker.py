#!/bin/python3

from stringlib import *

#Add a Worker class to this file.
class Worker:
    def __init__(self, str): #might remove self here if it reqs 2 params
        # body of the constructor
        self.str = str
        #print("Input String is " + str)
        #w1 = Worker(str) #hard coding string value here because I think we're supposed to
        #w1.        
#The Worker class constructor needs to take as input
#a string.  It will set its own data member to that string.
    def reverse_method(self):
        return reverseStr(self.str)
    
    def contains_method(self, str):
        return containsWord(self.str, str)

    def palindrome_method(self):
        return isPalindrome(self.str)

    def upperCase_method(self):
        return upperCaseStr(self.str)
#Add methods to the Worker class that are equivalent to
#functions in the stringlib module.  These methods will
#not take a string as input (except for the containsWord
#method, which will take the contained string parameter).  Instead,
#these methods will operate on the Worker class data member. 
#Your method can call the needed function in the stringlib
#module.

