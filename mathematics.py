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
   return x / y
   
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
    
