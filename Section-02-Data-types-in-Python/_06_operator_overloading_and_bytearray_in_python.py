# operator overloading 
# when operator is used for more than one task it is called operator overloading 
base_number = [1, 2, 3]
special_number = [7, 108, 1000]

total_number = base_number + special_number
# using + it concatenates 2 lists
print(f"using '+' in 'operator overloading' {total_number}")

black_coffee = ["2 gm coffee", "water"] * 3
# using * it multiplies list elements by the given input  
print(f"now use '*' in 'operator overloading' {black_coffee}")

# bytearray(b"single element") by this we can store only byte data; to perform any operation we need to work on bytes
single_name = bytearray(b"KRISH")
print(f"this is bytearray example {single_name}")

# we can change some characters of bytearray via replace; for that we need to store it in a new variable after the operation
change_name = single_name.replace(b"KRI", b"WFI")
print(f"after doing replace in bytearray example {change_name}")
