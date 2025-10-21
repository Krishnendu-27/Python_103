# `Problem 3`: Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.
cost_price = int(input("enter the cost ammount: "));
sale_price = int(input("enter the sale ammount: "));
if sale_price > cost_price:
    print("it is a profit ");
else:
    print("it is a loss ");
