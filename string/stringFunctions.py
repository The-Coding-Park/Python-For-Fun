str=input("enter a string: ")
print("your string is ","'",str,"'")


#functions
print("Converts the first character to upper case: ",str.capitalize())
print("Converts string into lower case: ",str.casefold())
print("	Returns a centered string: ",str.center())
print("	Searches the string for a specified value and returns the position of where it was found ",str.isalnum())
print("	Converts a string into lower case: ",str.islower())
print("Splits the string at the specified separator, and returns a list: ",str.split())
print("length of a string: ",len(str))


#Simple Index Based Formatting

print("My Name is {0}".format("Gunjan"))
print("I like {0} and {1}".format("Java", "Python"))
# same as above
print("I like {} and {}".format("Java", "Python"))
# index can be in any order
print("I like {1} and {0}".format("Java", "Python"))


#maketrans() with one argument

s = 'ABCDBCA'

translation = s.maketrans({ord('A'): 'a', ord('B'): ord('b')})  # single argument as dict
print(s.translate(translation)) 
#Python String translate() with manual mapping

s = 'ABCDBCA'

print(s.translate({ord('A'): ord('a'), ord('B'): ord('b'), ord('C'): None}))
print(s.translate({ord('A'): 'X', ord('B'): 'YZ', ord('C'): None}))

#indexing of string
print(str[1])
#negative indexing
print(str[-1])
