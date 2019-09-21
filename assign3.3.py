score = input("enter score (0.0 ~ 1.0) :")
if float(score) < 0.0:
    print("error")
    quit()
if float(score) > 1.0:
    print("error")
    quit()
elif float(score) < 0.6:
    print("F")
elif float(score) <= 0.7:
    print("D")
elif float(score) <= 0.8:
    print("C")
elif float(score) <= 0.9:
    print("B")
elif float(score) <= 1:
    print("A")
