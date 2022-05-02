def ValidationQuantity():# here i am validating the Quantity max 5
    Quantity=eval(input("ENter quantity"))
    while Quantity<0 or Quantity>5:
        print("Quantity is invalid, please try again")
        Quantity=eval(input("ENter quantity"))

    return Quantity

def calculate(Quantity):#here i am getting the price and calculating the max value,Total prices, postdiscount and the discount
    prices=[]
    for i in range (0,Quantity):
        price=eval(input("ENter price"))
        prices.append(price)

    Highest=max(prices)#getting the maxi prices 
    TotalPrice=sum(prices)# calculating the total 
    if TotalPrice>40:#Condition part if greater than 40 discount applies 
        Discount=TotalPrice*0.05
        PostDiscount=TotalPrice-Discount#post discount calculation
    else:
        Discount=0
        PostDiscount=TotalPrice

    return Highest,TotalPrice,Discount,PostDiscount
def displAY(Highest,TotalPrice,Discount,PostDiscount,Name):#here i am displaying the Highest,TotalPrice,Discount,PostDiscount,Name
    if TotalPrice>40:
        print("Hello,",Name,",the most expensive product you bought is ",Highest,"and your Total grocery bill is ",TotalPrice,"you qualify for a discount of ",Discount,"and your post discount bill is",PostDiscount)
    else:
         print("Hello,",Name,",the most expensive product you bought is ",Highest,"and your Total grocery bill is ",TotalPrice,"you do not qualify for a dsicount")

def main():# the main application starts here 
    Name=input("enetr your Name")# here I am getting the name 
    Quantity=ValidationQuantity()
    Highest,TotalPrice,Discount,PostDiscount=calculate(Quantity)
    displAY(Highest,TotalPrice,Discount,PostDiscount,Name)
    

main()# I am calling the main application

        
