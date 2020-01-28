import math 
def root(a,b,c):
    if (a==0):
        print("invalid root")
        return -1
    d=b**2-(4*a*c)
    if(d>0):
        print("1st root: ",(-b-d)/(2*a))
        print("2nd root: ",(-b+d)/(2*a))
        return -1
    elif(d==0):
        print("Root:",-b/(2*a))
    else:
        print("Roots are complex") 
        print(- b / (2*a) , " + i", d) 
        print(- b / (2*a) , " - i", d) 

print("Equation: ax*2 + bx + x =0")
a=int(input("value of a: "))
b=int(input("value of b: "))
c=int(input("value of c: "))
root(a,b,c)