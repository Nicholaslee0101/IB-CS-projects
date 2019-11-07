#Section 1

print(9 % 7)
print((8 * 4) - 4)
print(bool(4))
print(abs(-1 * 10) + 4 )
print(pow((4 % 4), 2) + 1)
print(20-int(14.5))
print(bool(int(2.2)*5-10))
print(divmod(19,4))
print(str((5*10) - (13 + 5)))
print(float(int(True) + 4 - (15 % 4)))

#Question 1: Float and Integer
#Question 2: True and False
#Question 3: var1 =+ 1 (saves memory and time)

#Section 2
print(4 > 3 and 2 > 1)
print(len('Hi') < 3)
print(6 < 8 or 12 > 10)
print(not 7 > 10)
print(5 > 6 and 8 < 7)
print(not (6 > 5 and 8 < 7))
print('A' != 'B' and (10/2 == 5))
print('A' == 'B' and (10/2 != 5))

#Snippet 1
a = 10
b = 100 + 1
print (a,b)

#Snippet 2
var_one = 100
var_two = 50
print(var_one + 10)

#Snippet 3
a = 1
b = 10
a = a+b
a = a*2
print(a)

#Snippet 4
my_name = 'Mr. Bach'
your_name = 'Mr. Student'
print('Is your name', my_name + ' or ' + your_name,'?')

#Snippet 5
this_val = False
that_val = True
some_val = 0
this_val = 1
print(this_val)
print(this_val > that_val )
print(some_val + 0)

#Question 1:

a = 5
b = 3
c = 3

print(-b +- (b** - 4*a*b)**0.5/2*a)

##############################################################################################

import math

a,b,c = input("Enter the coefficients of a, b and c separated by commas: ")

d = b**2-4*a*c # discriminant

if d < 0:
    print("This equation has no real solution")
elif d == 0:
    x = (-b+math.sqrt(b**2-4*a*c))/2*a
    print("This equation has one solutions: ", x)
else:
    x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
    x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
    print("This equation has two solutions: ", x1, " and", x2)

##############################################################################################

#Questions 2:
a = True
b = True
c = True
x = a and b or not a or c
print(x)
