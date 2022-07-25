# Given a text file, which contains few lines.WAP in python to remove 
# all the articles (a,an,the)and store in another file

file = open(r"Sem 2 Practicals\Python programs CP 2nd Sem\2_1.txt", "r")
data = file.read()
file.close()
data = data.split()

file = open(r"Sem 2 Practicals\Python programs CP 2nd Sem\2_2.txt", "w")
for i in data:
    if i == 'a' or i == 'an' or i =='the':
        pass
    else:
        file.write(i+' ')
file.close()