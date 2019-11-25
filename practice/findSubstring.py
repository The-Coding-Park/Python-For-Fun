string=input("enter the main string: ")
substring=input("enter the substring: ")
c=0
str=string.split()
if(len(str)>1):
    for i in str:
        if(i==substring):
            print("loc is ",c+1)
        c=c+1
else:
    print("loc is ",1)
