count = 0
while count < 10:
    count = count + 1
    print(count*10)


count = 0
while count < 5.3:
    count = count + 0.2
    print(round(count, 1))

a = 1
b = 2
for i in range(0, 5):
    a = b * a + i
print(a)

for d in range(0,101):
    if d%3 != 0 and d%8 != 0:
        print(d)

height = 5
print(height * ' ' + '*')
for i in range(1, height):
  print((height - i) * ' ' + '*' + (2*i-1) * ' ' + '*')

for i in range(2, height):
  print(i * ' ' + '*' + (2*(height-i)-1) * ' ' + '*')
print(height * ' ' + '*')

### warm up question
number = 10
while number != 0:
    number /= 2
    print(number)
