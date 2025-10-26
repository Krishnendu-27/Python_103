# String - Core, Indexing, Slicing, and Encoding

# Strings are immutable

coustomer_name = "antika"
coustomer_order = "aromatic bold tea"

# In Python, each character has an index starting from 0.
# Slicing uses [start:end:step], and the end index is exclusive.
print(f"The order of {coustomer_name} is {coustomer_order}")

# Full string from index 0 to end
print(f"Full string: {coustomer_order[0:]}")

# From beginning up to (but not including) index 17
print(f"Up to index 17: {coustomer_order[:17]}")

# Every 5th character from index 0
print(f"Every 5th char: {coustomer_order[0::5]}")

# Reverse the entire string
print(f"Reversed string: {coustomer_order[::-1]}")

# Encoding and decoding
lable = "Happy birthday 😇"
encode_lable = lable.encode("utf-8")  # str -> bytes
# decode_lable = lable.decode('utf-8')  # ❌ Error: lable is already a str
decode_lable = encode_lable.decode('utf-8')  # bytes -> str

print(f"Original label: {lable}")
print(f"Encoded label: {encode_lable}")
print(f"Decoded label: {decode_lable}")
