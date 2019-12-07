name = input("Enter file:")
if len(name) < 0 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
words = list()
for line in handle:
    line = line.strip()
    if line.startswith('From '):
        word = line.split()
    words.append(word[1])
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    print(counts)






#     for words in word:
#         counts[words] = counts.get(words,0) + 1
#     for words,count in counts.items() :
#         if bigcount == None or count > bigcount :
#              bigword = words
#              bigcount = count
# print(bigword, bigcount)

