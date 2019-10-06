hour = input("enter hour")
rate = input("enter rate per hour")
hour = float(hour)
rate = float(rate)

def computepay(hour, rate):
    if hour <= 40 :
        pay = hour * rate
        return pay
    else :
        pay = rate*(1.5*hour-20)
        return pay
  
print(computepay(hour,rate))
    
