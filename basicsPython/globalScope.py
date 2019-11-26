#global initialization
a=int(input("enter global value of a: ")) 
def check():
    print("inside the function")
    #scope of this a is bounded in function
    a=int(input("enter value of a : "))
    print("value of a from function: ",a)
check()
print("global value of a: ",a)
    