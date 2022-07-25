# Write a program that lets the user 
# enter a string and displays the character that appears most 
# frequently in the string.

text = input("Enter a string: ")
lst = text.strip()
dct = {}
for i in lst:
    if i in dct.keys():
        dct[i] += 1
    else:
        dct[i] = 1
max = list(dct.values())[0]
key = list(dct.keys())[0]
for i in dct:
    if dct[i] > max:
        max = dct[i]
        key = i
    else:
        pass
print('Character having highesh frequecy is', key, 'with frequency', dct[key])