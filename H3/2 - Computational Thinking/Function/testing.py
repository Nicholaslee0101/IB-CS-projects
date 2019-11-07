def func1 (name):
    print('Hi ' + name)

func1('Bill')
func1('KILROY')
func1('Susan')

def func2(a,b,c):
    print(a * b + c)

func2(5,1,2)
func2(10,2,-1)
func2('A',3,'K')
func2(6.7,0.002,1.2)

def func3(var1,var2):
    var1 *= 100     #var1 = var1 * 100
    var2 += var1    #var2 = var2 + var1
    return var2

new_var = func3 (5,10)
print(new_var)
print(func3(100,1000))

def greet(first, last):
    return 'Hi ' + first + ' ' + last + ', I never liked you.'
print (greet('Bill', 'Weld'))
