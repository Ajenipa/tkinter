def dollar(num):
    return num * 360
def pounds(num):
    return num * 400
currency=input("enter currency:")
num=float(input("enter amount:"))
if currency == "$":
    print(dollar(num))
else:
    print(pounds(num))