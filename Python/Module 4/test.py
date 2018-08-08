def getDiscount(age):
    discount = 0
    if age > 60 and age < 70:
        discount = 15
    elif age > 70:
        discount = 30 
    return discount
myAge = int(input("Enter Age:"))
myDiscount = getDiscount(myAge)
print("Discount percent=",myDiscount)
 
