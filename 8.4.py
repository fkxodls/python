fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    #print(line)
    words = line.split()
    #print(words)
    for word in words:
        # print(word)
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)


