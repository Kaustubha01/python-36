n = int(input("Enter the number"))

def isPrime(n):
    if (n <= 1):
        return False
        
        for i in range(2, n):
        if (n % i == 0):
            return False
        else  return True
    
            if isPrime(n):
    print("Prime")
else:
    print("Not a prime")
