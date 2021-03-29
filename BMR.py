name = input("please insert your name : ")
gender = input("please insert your gender : ")
age = int(input("please insert your age :"))
Height = int(input("please Enter Height : "))
Weight = int(input("please Enter Weight : "))

#BMRm for male 

BMRm = ((age*6.8)-(Height*5)+(Weight*13.7)+66)
BMRm1 = round(BMRm,2)

#BMRf for female 
BMRf = ((age*4.7)-(Height*1.7)+(Weight*9.66)+65.5)


BMRf1 = round(BMRf,2)
if gender == "male" :
    print(f"mr {name} ,you Calories need :{BMRm1}")
   
else :
    print(f"ms {name} you Calories need : {BMRf1}") 