text = "X-DSPAM-Confidence:    0.8475";
a = text.find('    ')
b = text.find('5',a)
fin = d=text[a+1 : b+1]
fin = float(fin)
print(fin)