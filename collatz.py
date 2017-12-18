#!/usr/bin/python

# COLLATZ SEQUENSE:


def collatz(number):
    if number % 2 == 0:
        return_value = number // 2   
    else:
        return_value = number * 3 + 1
    
    print(return_value)
    return return_value


while True:
    try:
        number = int(input("Enter the number "))
        break
    except ValueError:
        print("The Input must be an Integer!")

ret = number

while True:
    ret = collatz(ret)
    if ret == 1:
        break
