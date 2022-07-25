# given a text file, which contains few integers and few stings.
# wap in python to select all the prime numbers form the file and store them in another file.

def prime(n):
    if n<=1:
        return False
    p = True
    for i in range(2, n//2+1):
        if n//i == n/i:
            p = False
    return p

file = open(r"Sem 2 Practicals\Python programs CP 2nd Sem\1_1.txt", "r")
data = file.read()
file.close()
data = data.split()

newData = []

for i in data:
    try:
        a = int(i)
        newData.append(a)
    except:
        pass

newestData = []

for i in newData:
    a = prime(i)
    if a == True:
        newestData.append(i)

file = open(r"Sem 2 Practicals\Python programs CP 2nd Sem\1_2.txt", 'w')
for i in newestData:
    file.write(str(i)+'\n')
file.close()

print(newestData)