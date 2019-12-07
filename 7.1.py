# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
stxt = fh.read()
Upc = stxt.upper()
Upc = Upc.strip()
print(Upc)