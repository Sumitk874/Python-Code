string = input("Enter the string to be checked\n")
start = input("Enter the first letter of string to check if it starts with that\n")

startsWith = lambda x : True if x.startswith(start) else False
print(startsWith(string))
