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
    The Lazy Caterer’s Sequence -  describes the maximum number of pieces (or bounded/unbounded regions) of a circle (a pancake or pizza is usually used to describe the situation) that can be made with a given number of straight cuts.
    """

    if n < 0:
        return None
        
    piece_count = (n*n+n+2) / 2
    
    return piece_count 
   
   
"""
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user 
choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")
"""
