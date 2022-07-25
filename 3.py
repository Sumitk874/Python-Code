# Given a text file, which contains few paragraphs. WAP in python to 
# append line number before every line and store it another file..Count 
# the no of lines in that file. A line which end with full stop(.) is counted 
# as one line.

file = open(r"Sem 2 Practicals\Python programs CP 2nd Sem\3_1.txt", "r")
data = file.read()
file.close()

dataLine = data.split('.')

for i in range(len(dataLine)-1):
    print(str(i+1)+'. '+dataLine[i]+'.')