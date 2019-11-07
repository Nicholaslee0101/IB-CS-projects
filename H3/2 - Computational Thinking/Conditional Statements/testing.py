#Task 1
number = 23.3
if number == int(number):
    print ('The input is an integer')
else:
    print('The number is not an integer')

#Task 2
def count_vowels(text):
    count = 0

    if 'a' in text:
        count += 1
    if 'e' in text:
        count += 1
    if 'i' in text:
        count += 1
    if 'o' in text:
        count += 1
    if 'u' in text:
        count += 1

    if count == 5:
        print('Got them all')
    elif count > 0:
        print('Got some')
    else:
        print('Got none')

count_vowels('aeiou')
count_vowels('aeio')
count_vowels('jklmn')

#Task 3
a = 10
b = 2
if a < b:
    print('YES')
else:
    print('NO')

###Ternary Statement###
a = 10
b = 2
print('YES') if a < b else print('No')

#Task 4
a = 2
b = 9
print('YES') if a < b else print('Winner') if a**b <= 100 else print('NO')

#Task 5
import math
a = 500
if math.sqrt(a) < 5 or math.sqrt(a) > 10 or a == 10:
    print('Yes because: ', end='')
    if math.sqrt(a) < 5:
        print('Square root less than 5')
    elif math.sqrt(a) > 10:
        print('Square root greater than 10')
    else:
        print('Is equal to 10')

#Task 6
a = 3
b = 7
if a == b - 4 == 3:
    print('Checks out')

