# def welcome():
#     print("Hello")

# welcome()

# def purple():
#     pass

# purple()

# def welcome(name):
#     '''Hello
#     Hi
#     Welcome'''
#     print("bye",name,"welcome to the party")

# print(welcome.__doc__)
# name1=welcome("Alexander")

# def sum(num1,num2):
#     add=num1+num2
#     print(add)
# a = 3
# b = 6
# numInput1 = int(input("Enter a number: "))
# numInput2 = int(input("Enter another number: "))
# sum(numInput1,numInput2)

# def greatest(num1,num2,num3):
#     if(num1 > num2 and num1 > num3):
#         print(num1 , " is the greatest number")
#     elif(num2 > num1 and num2 > num3):
#         print(num2 , " is the greatest number")
#     else:
#         print(num3 , " is the greatest number")

# a=3
# b=5
# c=7
# greatest(a,b,c)

# def power(a,b):
#     return a**b

# var = power(4,2)
# print(var)
# a=50
# def value():
#     # a=50
#     global a
#     a = 50
#     print("inside the function, the value of a is ", a)
# value()
# print("outside the function, the value of a is ", a)

def hi():
    print("hello")
hi()
del hi
print("after deleting the function")
hi()