from decimal import DivisionByZero

#try block is always run first if it throws an exception it goes to the else block block. 
#if there is no exception it will go to ecxept block.
#finally block always runs
# try:
#     print("try block")
#     num1 = int(input("Enter the first number"))
#     num2 = int(input("Enter the second number"))
#     res=num1/num2

# except DivisionByZero:      #divisionByZero is optional. if you don't write that it still will gt executed
#         print("Except block")
#         print("number 1 is not divisible by 0")

# else:
#     print("else block")
#     print("output", res)

# finally:
#     print("Exception handling")

try:
    x=int(input("Enter you age: "))
    if x<18:
        raise ValueError
except ValueError:
    print("You are out of range")
else:
    print("You are within the range")
finally:   
    print(x)    