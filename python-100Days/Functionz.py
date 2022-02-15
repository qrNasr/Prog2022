
## important functions in python

a=13
print(dir(a)) # use dir functions to see all functions/methodes with any object or variable
print(dir(a))
a='13'
print(type(a)) # to see which class this variable belongs 2
#now use help to see the class methodes of alls string()
print(help(str))
## now search for any function within the class
print(help(str.lower))
print(help(str.upper()))
print(help(str.capitalize))
print(help(str.center()))
##id methode
print(id(a)) ## memeory id

# type casting methodes

print(int(4.5))
print(float(4))
print(bool(-1)) ## all numbers are tue,even negative number, except 0 which is false
print(chr(67))
print(str(4))
print(eval("[1,2]")) ##evaluate expression
print(eval("4**2+1"))
print(complex(4,8)) # 4 is real, 8 is imaginary

## change between numbering system
d=13
print(bin(d)) # change to Binary
print(oct(d)) ## change to octal
print(hex(d))## change to hexadecimal


## Bitwise operator (and, or etc ..)
# used for ip address chanage
ip= 192
mask= 255
ip_mask = ip& mask # will add and to bits
print(bin(ip_mask))


## divmod function
print(divmod(10,2)) ## return the product and remainder
print(divmod(10,3)) ## return the product and remainder

## solve quadratic 
a=1
b=5
c=6
m =pow((b**2-4*a*c),0.5)
x1=(-b+m)/2*a
x2=(-b-m)/2*a
print(x1,x2)





































