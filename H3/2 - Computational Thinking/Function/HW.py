#Question 1
def mixed_number (a, b):
    return str(a//b) + " " + str(a%b) + '/' + str(b)

print (mixed_number(14,4))

#Question 2
def vowel_count_1 (a):
    var1 = a.count('a')
    var2 = a.count('e')
    var3 = a.count('i')
    var4 = a.count('o')
    var5 = a.count('u')
    return var1 + var2 + var3 + var4 + var5

print(vowel_count_1('Mr Bach is awesome'))

#Question 3
def vowel_count_1 (a):
    var1 = a.count('a')
    var2 = a.count('e')
    var3 = a.count('i')
    var4 = a.count('o')
    var5 = a.count('u')
    return var1,var2,var3,var4,var5

a,e,i,o,u = vowel_count_1('Mr Bach is awesome')
print(a,e,i,o,u)

#Question 4
import math
def volume_of_volume(a):
    var1 = 4/3 * math.pi * a**3
    return round (var1, 2)

print (volume_of_volume(10))

def sphere_surface_are(a):
    var2 = 4 * math.pi * a**3
    return round (var2, 2)

print (sphere_surface_are(10))

#Question 5
import math
def volume_of_volume(a):
    var1 = 4/3 * math.pi * a**3
    return round (var1, 2)

print ('Sphere Volume:', volume_of_volume(10))

def sphere_surface_are(a):
    var2 = 4 * math.pi * a**3
    return round (var2, 2)

print ('Sphere Surface Area:', sphere_surface_are(10))

#Question 6
def name_funcation(name, msg = "38", msg2 = '43'):
    print(name + ' ' + msg + ' ' + msg2)

name_funcation("Ted")
name_funcation("Ted", "34")
name_funcation("Teddy", "75" , "56")

#Question 7
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def rgb_to_hex( r, g, b ):
    return '#%02x%02x%02x' % (r, g, b)

print('Please enter your colour hex')

hex = input()

print(hex_to_rgb(hex))

print('Please enter your RGB color (R, G, B)')
r = int(input())
g = int(input())
b = int(input())
print(rgb_to_hex(r, g, b))