# how to creat string use ' ' and " " and also """ """ and str("write string")
a = "ab"
b = 'cd'
c = """ hi """
#why need this 3 
# senetcnce problem 
# a = "hi ' am krish"
# tripple invided use for multiline command
e = str("hi bro")

# python internally assign each charcater a index like "hi" h = 0 i = 1 its called positive indexing and we can extract any charcetr via index
g = "my name is K"
print(g[5]) # m 
# python also give negative idexing mens it give -1 the last chacrert and its goes bcakward
print(g[-1]) # K
# slicing : when we need one or more chacrter we use slicing it need a range
print(g[0:6]) # my nam 
# we can skip on side 
print(g[0:]) # my name is k 
print(g[:4]) # my n 
# for skiipping any index
print(g[0::2])
# for reversing a string just use ::-1
print(g[::-1])
# in python string are inmutable

