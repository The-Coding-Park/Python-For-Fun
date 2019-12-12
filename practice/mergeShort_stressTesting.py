import random
def merge(arr):
    if(len(arr)>1):
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        merge(L)
        merge(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            if(L[i]<R[j]):
                arr[k]=L[i]
                i=i+1
            else:
                arr[k]=R[j]
                j=j+1
            k=k+1
        while i<len(L):
            arr[k]=L[i]
            i=i+1
            k=k+1
        while j<len(R):
            arr[k]=R[j]
            j=j+1
            k=k+1
t=random.randint(5,10)

print("No. of test case: ",t)
while(t>0):
    n=random.randint(1,100)
    print("number of elements: ",n)
    arr=[]
    for i in range (n):
        arr.append(random.randint(1,1000))
    merge(arr)
    print(arr)

    t=t-1