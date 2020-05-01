def dollar(num):
    return num * 360
def pounds(num):
    return num * 400
def euros(num):
    return num * 420
currency=input("enter currency:")
num=float(input("enter the amount you wish to convert:"))
if currency =="dollar" and currency != "euros" and currency != "pounds":
    print("your money in naira is #" +str(dollar(num)))
elif currency == "pounds" and currency != "dollar" and currency != "euros":
    print("your money in naira is #"+str(pounds(num)))
elif currency == "euros" and currency != "dollar" and currency != "pounds":
    print("your money in naira is #"+str(euros(num)))
while currency != "pounds" and currency != "dollar" and currency != "euros":
    print("WRONG CURRENCY")
    break