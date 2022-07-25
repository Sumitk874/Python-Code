def stringRem():
    string = input("Enter a String\n")
    n = int(input("Enter the index to be removed\n"))


    first = string[0:n]
    last = string[n+1:]
    print(first+last)

stringRem()
