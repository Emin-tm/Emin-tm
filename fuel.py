Gsc = int(input("please insert your  Gasoline consumed car :"))
#Gsc is gasoline consumed
kms = int(input("please insert Kilometers traveled :"))
#kms is the covered distance ،kms

Fsc = Gsc * 100
lofg = Fsc / kms
fuel = round(lofg,2)

if fuel < 6 :
    print(f"Your car {fuel} consumes, is less fuel")
   
elif fuel < 9 :
    print(f"Your car {fuel}  consumes, is  normal fuel")
   
else :
    print(f"Your car {fuel} consumes, is a lot of fuel")