hour = input("enter hour")
rate = input("enter rate per hour")
if float(hour) <= 40.0:
    pay = float(hour)*float(rate)
elif float(hour) > 40.0:
    pay = 40.0 * float(rate) + (float(hour) - 40.0)*1.5*float(rate)
print("pay:", pay)