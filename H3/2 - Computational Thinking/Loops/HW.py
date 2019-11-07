#Question 1
def both():
    # section 1
    for a in range(8,-4,-1):
        print(a)
    # section 2
    count = 8
    while count > -4:
        print(count)
        count -= 1
both()

#Question 2
def is_odd(i):
    if i%2==0:
        return False
    else:
        return True

def main():
    for i in range (1,11):
        if is_odd(i) == True:
            print("Odd")
        else:
            print("Even")

main()

#Question 3
import random
def dice_roll(q):
    count = 0
    sumofdice = 0
    while sumofdice != q:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice3 = random.randint(1, 6)
        count += 1
        sumofdice = dice1 + dice2 + dice3
    print(count)

dice_roll(17)

#Question 4
def odd_even_count(a):
    odd = 0
    even = 0
    while a != 0:
        # step 1
        if is_odd(a%10) == True:
            odd += 1
        else:
            even += 1
        # step 2
        a = int(a/10)
    print('Odd:', odd, 'Even:', even)

def is_odd(i):
    if i%2==0:
        return False
    else:
        return True

odd_even_count(789319231)
odd_even_count(987654)

#Question 5
def string_analysis(str):
    letter = 0
    digit = 0
    space = 0
    for character in str:
        if character == " ":
            space += 1
        elif character >= "0" and character <= "9":
            digit += 1
        elif (character >= "A" and character<= "Z") or (character >= "a" and character<= "z"):
            letter += 1
    print("Letter:", letter, "Digit:", digit, "Space:", space)

string_analysis("I'm not 89 years old")