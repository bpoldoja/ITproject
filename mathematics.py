import hashlib

def add(x, y):
   return x + y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
    a = 0
    result = 0
    pos = True
    if x == 1:
        return y
    elif y == 1:
        return x
    elif x > 0 and y < 0:
        pos = False
        y = y * (-1)
    
    elif x < 0 and y > 0:
        pos = False
        y = y * (-1)    
    
    elif x < 0 and y < 0:
        y = y * (-1)
        x = x * (-1)
    
    elif x ==0 or y == 0:
        return 0
       
        
    while a < y:
        result = result + x
        a += 1
        
    if not pos:
        result = result * (-1)
    
    return result

# This function divides two numbers
def divide(x, y):
    try: return x / y
    except ZeroDivisionError:
        return None
   
def hashing(x):
    """
    Input hashing dependant on the length of the input

    """
    x = x.encode(encoding='UTF-8')
    if len(x) < 5:
        hash_result = hashlib.sha1(x)
        #print('sha1')
    elif len(x) == 5:
        hash_result = hashlib.md5(x)
        #print('md5')
    elif len(x) <= 25:
        hash_result = hashlib.sha256(x)
        #print('sha256')
    elif len(x) == 38:
        hash_result = hashlib.sha384(x)
        #print('sha384')
    else:
        hash_result = hashlib.sha512(x)
        #print('sha512')
        
    return hash_result.hexdigest()


def fib(n):
    """
    Fibonacci sequence calculator

    """
    if n < 0:
        return None
    elif n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        return fib(n-1)+fib(n-2)
        
def pie(n):
    """
    The Lazy Caterer’s Sequence -  describes the maximum number of pieces (or bounded/unbounded regions)
    of a circle (a pancake or pizza is usually used to describe the situation) that can be made with a 
    given number of straight cuts.

    """

    if n < 0:
        return None
        
    piece_count = (n*n+n+2) / 2
    
    return piece_count 
   

def powerof(base, maxi):
    """
    Calculates the power of numbers

    """
    counter = 1
    res = base 
    if maxi == 0:
        return 1

    while counter < maxi:
        counter = counter + 1
        res = multiply(res, base)

   
    return res

def arrayof(base, maxi):
    """
    Shows all the temporary values of taking to the power of given value

    """

    counter = 0
    array = []

    while counter <= maxi:
         array.append(powerof(base, counter))
         counter = counter + 1

    return array

def factorial(n):
    """
    Calculates the factorial of a number
    
    """
    num = 1

    while n >= 1:
        num = num * n
        n = n - 1

    return num


    
# Take input from the user 
choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10):")

if choice == '1':
   num1 = int(input("Enter first number: "))
   num2 = int(input("Enter second number: ")) 
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   num1 = int(input("Enter first number: "))
   num2 = int(input("Enter second number: "))
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   num1 = int(input("Enter first number: "))
   num2 = int(input("Enter second number: ")) 
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   num1 = int(input("Enter first number: "))
   num2 = int(input("Enter second number: ")) 
   print(num1,"/",num2,"=", divide(num1,num2))

elif choice == '5':
   txt = input("Enter text: ") 
   print("Text:",txt, hashing(txt))

elif choice == '6':
   num3 = int(input("Enter number: "))
   print("Fibonacci:",num3,"=", fib(num3))

elif choice == '7':
   num3 = int(input("Enter number: ")) 
   print("Pie:",num3,"is", pie(num3))

elif choice == '8':
   num1 = int(input("Enter first number: "))
   num2 = int(input("Enter second number: ")) 
   print("Power of",num1,"^", num2,"=",powerof(num1,num2))

elif choice == '9':
   num1 = int(input("Enter first number: "))
   num2 = int(input("Enter second number: ")) 
   print("Array of",num1,"^", num2,"=", arrayof(num1,num2))

elif choice == '10':
   num3 = int(input("Enter number: "))  
   print("Factorial",num3,"is", factorial(num3))
else:
   print("Invalid input")



              
