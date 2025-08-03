#  Objects - Mutable and Immutable in Python

everything is a object
verey object has 
1. identity
2. type 
3. value

so in python see the object is *mutable or not* is best way to see this by identity 
if idenenty same its not mutable 
if idenenty not change  its  mutable

id() shows you the memory reference of the object currently being used.

If an integer hasn’t been used yet, Python will still create it when needed.

Reassigning a variable doesn’t mutate the integer; it just points the variable name to a new integer object.

Integers are immutable.

Even if you never explicitly use a number like 152, id(152) works because Python creates it on demand.

# Numbers, Booleans and Operators in Depth in Python

in python there are 4 types of number 
1. Integer
2. Boolean
3. Real floating-> Decimal
4. complex Number (for scienties use only ) 2+5j