ma = input("Podaj masę ciała:")
wz = input("Podaj wzrost:")
BMI = float(ma)/(float(wz)) ** 2
print ("BMI = " + str(BMI))
if BMI < 18.5:
    print("Niedowaga")
elif BMI < 25:
    print("Waga prawidłowa")
elif BMI < 30:
    print("Nadwaga")
else:
    print("Otyłość")