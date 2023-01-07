# This is implementation of recursion
# Program for factorial using recursion might not work for big numbers
def fact(x):
    if x==0:
        return 1
    elif x==1:
        return 1
    else:
        return x*fact(x-1)

x = int(input("enter number : "))
print ('factorial of {} is {} '.format(x,fact(x)))

