# WAP to enter five numbers and find the maximum number using simple if
'''a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
c = int(input('Enter third number:'))
d = int(input('Enter fourth number:'))
e = int(input('Enter fifth number:'))
if a>b and a>c and a>d and a>e:
    print('The maximum number is:',a)
elif b>a and b>c and b>d and b>e:
    print('The maximum number is:',b)  
elif c>a and c>b and c>d and c>e:
    print('The maximum number is:',c)   
elif d>a and d>b and d>c and d>e:
    print('The maximum number is:',d)   
elif e>a and e>b and e>c and e>d:
    print('The maximum number is:',e)'''




# WAP to enter five numbers and find the minimum number using simple if
'''a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
c = int(input('Enter third number:'))
d = int(input('Enter fourth number:'))
e = int(input('Enter fifth number:'))
if a<b and a<c and a<d and a<e:
    print('The minimum number is:',a)
elif b<a and b<c and b<d and b<e:
    print('The minimum number is:',b)  
elif c<a and c<b and c<d and c<e:
    print('The minimum number is:',c)   
elif d<a and d<b and d<c and d<e:
    print('The minimum number is:',d)   
elif e<a and e<b and e<c and e<d:
    print('The minimum number is:',e)'''
    



# WAP to convert a character to its ASCII equivalent
'''x = input('Enter a character:')
print('The ASCII equivalent of the "+x+" is ',ord(x))'''




# WAP to find the sum of natural numbers
'''num = 10
if num < 0:
   print("Enter a natural number")
else:
   sum = 0
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)'''




# WAP to calculate the factorial of any number
'''num = int(input('Enter a number:'))
factorial = 1
if num<0:
    print('Factorial does not exist')
elif num==0:
    print('Factorial of 0 is 1')
else:    
   for i in range(1,num+1):
    factorial = factorial * i
    print("The factorial of",num,"is",factorial) '''




# WAP to calculate the fibonacci series 
'''terms = int(input('Enter number of terms:'))
n1 = int(input('Enter the first term:'))
n2 = int(input('Enter the second term:'))
count = 0
if terms<=0:
    print('Enter positive number')
elif terms == 1:
    print('Fibonacci series upto',terms,':')
    print(n1) 
else:
    print('Fibonacci series:')   
    while count<terms:
        print(n1) 
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1'''





# WAP to find LCM,HCF,
'''def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm
num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))  
print("The L.C.M. is", compute_lcm(num1, num2))

def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf
num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))  
print("The H.C.F. is", compute_hcf(num1, num2))'''




# WAP to find leap year
'''year = int(input('Enter the year:'))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))'''




# WAP to find the Armstrong number
'''num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")'''




# WAP to find the palindrome number
'''n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")'''