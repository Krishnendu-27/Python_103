'''
 Problem 1: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:

 Salary(Lakhs) : Tax(%)

   Below 5 : 0%
   5-10 : 10%
   10-20 : 20%
   aboove 20 : 30%
'''
salary = int(input("enter your Salary in Lakhs"));
total_salary = salary - (salary*10/100) - (salary*5/100) - (salary*3/100);
if total_salary < 500000:
    tax_ammount = total_salary * 0/100
    print(f"Your  tax ammount is {tax_ammount} so your salry after deduction of tax {total_salary-tax_ammount}")
elif total_salary > 500000 and total_salary < 1000000:
    tax_ammount = total_salary * 10/100
    print(f"Your  tax ammount is {tax_ammount} so your salry after deduction of tax {total_salary-tax_ammount}")
    
elif total_salary > 1000000 and total_salary < 2000000:
    tax_ammount = total_salary * 20/100
    print(f"Your  tax ammount is {tax_ammount} so your salry after deduction of tax {total_salary-tax_ammount}")
    
else:
    tax_ammount = total_salary * 30/100   
    print(f"Your  tax ammount is {tax_ammount} so your salry after deduction of tax {total_salary-tax_ammount}")