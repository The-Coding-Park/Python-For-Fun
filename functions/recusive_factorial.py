def factorial(n):
    if (n==0):
        return 1
    return n*factorial(n-1);
a=int(input("enter the value to calculate factorial: "))
print(factorial(a))