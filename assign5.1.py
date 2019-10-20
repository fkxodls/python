lnum = None
snum = None

while True:
    num = input("enter a number ")

    if num == 'done':
        break 
    
    try:
        num = int(num)

    except:
        print('invalid value')
        continue

    if  lnum == None:
        lnum = num
        snum = num

    elif num > lnum:
        lnum = num

    elif num < snum:
        snum = num   

print("Maximum is",lnum)
print("Minimum is",snum)
