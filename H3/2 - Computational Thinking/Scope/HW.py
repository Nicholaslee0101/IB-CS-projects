#Question 1
a = 34
b = 16
c = 17
d = 22
e = 32

#Question 2
def add(num1, num2):
  return num1 + num2

def triple(num):
  return add(num, add(num, num))

def quadruple(num):
    return add(add(num, num), add(num, num))

print(add(2,3))
print (triple(3))
print (quadruple(2))
