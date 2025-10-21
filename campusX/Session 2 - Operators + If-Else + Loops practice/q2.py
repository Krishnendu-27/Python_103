# `Problem 2`: Write a program that take a user input of three angles and will find out whether it can form a triangle or not.

sidea = int(input("enter first side length: "));
sideb = int(input("enter seconed side length: "));
sidec = int(input("enter third side length: "));

if sidea + sideb > sidec and sideb + sidec > sidea and sidec + sidea > sideb:
    print(f"with {sidea} , {sideb} , {sidec} we can form triangle");
