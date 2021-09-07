# WAP using function
'''def fact(n):
    if n==0:
        result = 1
    else:
        result = n*fact(n-1)
    return result
print('Factorial of 4 is :',fact(4))
print('Factorial of 5 is :',fact(5))'''


# WAP using function
'''def add(v1,v2):
    print(v1+v2)
v1 = int(input('Enter first value'))
v2 = int(input('Enter second value'))
add(v1,v2)'''


# WAP using function
'''try:
    a = int(input('Enter first integer'))
    b = int(input('Enter second integer'))
    print(a/b)
except ZeroDivisionError as message:
    print('Please ensure that you can not divide any number by zero:',message)
except ValueError as message:
    print('Enter only integer number:',message) '''


# WAP using function 
'''try:
    a = int(input('Enter first integer'))
    b = int(input('Enter second integer'))
except (ZeroDivisionError) as message:
     print('There is no error in the try block')
finally:
    print('Final block is executed whether there is error or not')'''   


# WAP using nested function
'''def myname():
    print('My name is Dnyanada')
    def myrollno():
        print('My roll no is 7')
    myrollno()
myname()''' 


# WAP using function
'''def add_product(a,b):
    add = a+b
    product=a*b
    return add,product
x,y = add_product(200,50)
print('The addition is:',x)
print('The product is:',y)'''    


# WAP using default argument
'''def func(city='Nagpur'):
    print('I am from',city)
func('Delhi')
func('Pune')
func() '''


# WAP using import
'''import time
def msg():
    time.sleep(3)
    print('Hello World')
msg()
print('First call completed')
msg()
print('second call completed')
msg()
print('Third call completed')
msg()'''


# WAP using function
'''def func(fname,Iname):
    print('Hi',fname)
    print('Hi',Iname)
func(fname='Dnyanada',Iname='Moharir')'''


# WAP using function
'''def login():
    username = input('Enter your name')
    password = input('Enter your password')
    if username==password:
        print('Your login is succesful')
    else:
        print('Login failed')
login()'''


# WAP using lambda function
'''x = lambda a : a+10
print(x(5))
x = lambda a,b : a*b
print(x(3,2))
x = lambda x,y,z : x+y+z
print(x(10,20,30))'''


# WAP using function
'''def func(name):
    j=0
    for i in name:
        if i=='n':
            print('The character present at index number',j,'value is:',name)
            break
        j=j+1
name = input('Enter the name')
func(name)'''


# WAP using function
'''def info(first_name,last_name):
    print('First name=',first_name)
    print('Last name=',last_name)
info('Dnyanada','Moharir')'''


# WAP for addition,subtraction,multiplication,division using function
'''def add(a,b):
    print('Addition=',a+b)
result = add(20,30)   
def sub(a,b):
    print('Subtraction=',a-b)
result = sub(50,30)
def mul(a,b):
    print('Multiplication=',a*b)
result = mul(7,4)
def div(a,b):
    print('Division=',a/b)
result = div(20,5)'''


# WAP using for loop
'''for i in range(1,5):
    for j in range(1,4):
        print(i , end=' ')
print( )'''


# WAP to check even or odd using function
'''def check_even_odd(number):
    if number%2==0:
        print(number,'This is an even number')
    else:
        print(number,'This is an odd number')
check_even_odd(20)            
check_even_odd(31)'''



# WAP 


