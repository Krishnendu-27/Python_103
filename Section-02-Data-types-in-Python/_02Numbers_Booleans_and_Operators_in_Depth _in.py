
import sys
from decimal import Decimal

# Integer arithmetic
poket_money_ram = 50
poket_money_sam = 70

total_poket_money = poket_money_ram + poket_money_sam
print(f"Total pocket money is: {total_poket_money}")

# After Ram bought 2 chocolates at ₹5 each
new_poket_money_ram = poket_money_ram - 10
print(f"Ram's remaining pocket money is: {new_poket_money_ram}")

# Division and modulo
mango_pieces = 53
servings = 2

each_person_get = mango_pieces / servings         # 26.5
# give us the exact answer by using /
round_up_quantity = mango_pieces // servings      # 26
# give us in integer  answer by using //
remaining_quantity = mango_pieces % servings      # 1

print(f"Each person gets: {each_person_get}")
print(f"Pieces per person (rounded down): {round_up_quantity}")
print(f"Remaining pieces: {remaining_quantity}")

# Multiplication
price_per_mango = 30

total_mango_price = mango_pieces * price_per_mango
print(f"Total price of mangoes: {total_mango_price}")

# Exponentiation
base = 2
exponent = 6
power_result = base ** exponent    # 2^6
print(f"{base} to the power of {exponent} is {power_result}")
# in python we can write number like  ⬇️ it only use for readibility 
total_num = 1_000_000_000_000_00;
print(total_num)

# Boolean values
milk_present = True
print(f"Is milk present? {milk_present}")

# Booleans in arithmetic (True → 1, False → 0)
milk_present_yesterday = 5

today_total_milk = milk_present_yesterday + milk_present
print(f"Total milk count today: {today_total_milk}")

# System float info (platform-dependent)
print(sys.float_info)

# High-precision decimals
large_decimal = Decimal('1.0000000000000000001') * Decimal('2.5')
print(f"High-precision result: {large_decimal}")
