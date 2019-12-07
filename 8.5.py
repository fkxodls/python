fname = input("Enter file name: ")
count = 0
fh = open(fname)
for line in fh:    
    line = line.rstrip()
    if line.startswith('From '):
        count = count + 1
        words = line.split()
        print(words[1])
print(count)
    
