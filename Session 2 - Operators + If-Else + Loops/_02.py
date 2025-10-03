# if else
# condtions it use for branchcing mens code goes 1 to last line for a diffrent senario we use diffrent condition

# programe check the login

email = input("enter the email ")
password = int(input("enter the password "))

if email== "o@gmail.com" and password == 1234:
    print("its correct! Welcome sir");
elif email== "o@gmail.com" and password != 1234:
    print("its correct! password is wrong");
elif email!= "o@gmail.com" and password == 1234:
    print("its correct! email is wrong");
else:
    print("its incorrect! Try again");
# in python induntation work as scope
# when we use if else within if else it called nested if else

# find min 3 number
num1 = int(input("enter the number 1 "))
num2 = int(input("enter the number 2 "))
num3 = int(input("enter the number 3 "))
if num1>num2 and num1>num3:
    print("the bigest number is number 1",num1);
elif num2>num1 and num2>num3:
    print("the bigest number is number 2",num2);
else:
    print("the bigest number is number 3",num3);

