
#1
i=0
while i<3:
    file = input("aaaaaa : ").strip()
    print(file)
    try:
        f = open("inFruit.txt", 'r')
        break
    except FileNotFoundError:
        import sys
        sys.stderr.write("No file: %s. Try Again\n" % file)
        i+=1
    
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
counts=[]

for j in range(26):
    counts.append(0)

contents = f.readlines()

for line in contents:
    for k in line:
        if k.isalpha() == True:
            counts[ord(k)-ord('a')]+=1

count = 0
while count<=25:
    for j in counts:
        print("{} : ".format(count+1),alphabet[count], 'appears {} times'.format(j))
        count+=1



