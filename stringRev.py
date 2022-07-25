def reverseString(string):
    reversed_string = ''
    for i in string:
        reversed_string = i + reversed_string
    
    print('Reversed String is', reversed_string)
 
reverseString(input())
