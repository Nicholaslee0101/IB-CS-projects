#Question 1
def driving_age(z):
    if z< 18:
        z = "False"
        return z
    else:
        z = "True"
        return z

print(driving_age(16))
print(driving_age(25))

#Question 2
def id_tringle(a, b, c):

    if a > b and a > c and b ** 2 + c ** 2 == a ** 2:
        x = 'right angle'
        return x

    if b > a and b > c and a ** 2 + c ** 2 == b ** 2:
        x = 'right angle'
        return x

    if c > b and c > a and b ** 2 + a ** 2 == c ** 2:
        x = 'right angle'
        return x

    if a > b and a > c and a ** 2 < b ** 2 + c ** 2:
        x = "Acute"
        return x
    if c > a and c > b and c ** 2 < a ** 2 + b ** 2:
        x = "Acute"
        return x
    if b > a and b > c and b ** 2 < c ** 2 + a ** 2:
        x = "Acute"
        return x

    if a > b and a > c and a ** 2 > b ** 2 + c ** 2:
        x = "Obtuse"
        return x
    if b > c and b > a and b ** 2 > a ** 2 + c ** 2:
        x = "Obtuse"
        return x
    if c > a and c > b and c ** 2 < b ** 2 + a ** 2:
        x = "Obtuse"
        return x

    else:
        x = 'This is not a triangle'
        return x

print(id_tringle(4, 3, 5))
print(id_tringle(12, 3, 54))
print(id_tringle(25, 3, 5))
print(id_tringle(50, 56, 74))

#Question 3
def fizzbuzz(a):
    if a%5 ==0 and a%3 == 0:
        a = 'FIZZ BUZZ!'
        return a

    if a%3 == 0:
        a = 'FIZZ!'
        return a

    if a%5 == 0:
        a = 'Buzz!'
        return a

    else:
        a = 'Huh?'
        return a

print(fizzbuzz(30))
print(fizzbuzz(5))
print(fizzbuzz(27))
print(fizzbuzz(7))

#Question 4
import random
def guess_dice(y, u, i):
    number1 = random.randint(1, 6)
    number2 = random.randint(1, 6)
    number3 = random.randint(1, 6)
    count=0
    if number1 == y :
        count+=1
    if number2 == u:
        count+=1
    if number3 == i:
        count+=1

    if count ==0:
        return "Rolled: " + str(number1) + ", " + str(number2)+ ", " + str(number3)+ ", with zero correct guesses"
    if count ==1:
        return "Rolled: " + str(number1) + ", " + str(number2)+ ", " + str(number3)+ ", with one correct guesses"
    if count ==2:
        return "Rolled: " + str(number1) + ", " + str(number2)+ ", " + str(number3)+ ", with two correct guesses"
    if count ==3:
        return "Rolled: " + str(number1) + ", " + str(number2)+ ", " + str(number3)+ ", with three correct guesses"

print(guess_dice(5, 3, 1))
print(guess_dice(6, 5, 4))

#Question 5
import random
def gimme_random(type, g, h):
    if type == 'int':
        g = int(g)            #make sure g is an integer
        h = int(h)            #make sure h is an integer
        number = int(random.randint(10, 56))
        return number
    if type == 'float':
        number = float(random.uniform(0.5, 1.9))
        return round(number,1)

print(gimme_random('float', 0.5, 1.9))
print(gimme_random('int', 10, 56))
