#find the max of three number using ternary operator
a,b,c=int(input("enter first value: ")),int(input("enter second value: ")),int(input("enter third value: "))
max=a if (a>b and a>c) else b if (b>c and b>a) else c
print(max)
