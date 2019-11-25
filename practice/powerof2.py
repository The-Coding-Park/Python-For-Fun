def is_power(n):
    n = n/2
    if n == 2:
        return True
    elif n > 2:
        return is_power(n)
    else:
        return False

num=int(input("Enter a number"))

if is_power(num):
    print ('yes')
else:
    print ('no') 