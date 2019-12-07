fname = input("Enter file name: ")
fh = open(fname)
total = 0.0
count = 0
for line in fh:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence: '):
        line = line.split()
        line = float(line[1])
        count = count + 1
        total = total + line
print(total/count)


    