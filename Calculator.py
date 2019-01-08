# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 22:30:35 2019

@author: SHIKHA
"""

print("Please select any operation: \n"\
     "+ \n"\
     "- \n"\
     "* \n"\
     "/ \n")

def add(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def multi(n1,n2):
    return n1 * n2
def div(n1,n2):
    return n1 / n2

select = input("Select any operation: ")

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

if select == "+":
    print("num_1 + num_2: " , add(num_1,num_2))
    
elif select == "-":
    print("num_1 - num_2: " , sub(num_1,num_2))
    
elif select == "*":
    print("num_1 * num_2: " , multi(num_1,num_2))
    
elif select == "/":
    print("num_1 / num_2: " , div(num_1,num_2))
    
else:
    print("Sorry, Invalid Input.")