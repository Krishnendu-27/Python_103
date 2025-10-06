'''
`Problem 4`: Write a menu-driven program -
1. cm to ft
2. km to miles
3. USD to INR
4. exit
'''
print("menu are: ");
print("1. cm to ft")
print("2. km to miles")
print("3. USD to INR")
print("4. exit")

option = int(input("enter the number: "))
if option == 1:
    cm = int(input("enter the cm: "))
    feet = cm / 30.48;
    print(f"{cm} cm in feet is {feet}")
elif option == 2:
    km = int(input("enter the km: "))
    miles =km * 0.621371;
    print(f"{km} km in miles is {miles}")
elif option == 3:
    usd = int(input("enter the USD: "))
    inr =usd * 88.83;
    print(f"{usd} usd in inr is {inr}")
elif option == 4:
    print("Exir succesfully")
else:
    print("enter correct number")