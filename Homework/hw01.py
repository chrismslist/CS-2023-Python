
## Partial credit will be given for code that passes the two given doctests. 
## For full credit on HW1 you should test your solutions to egypt(103,104) and  egypt(123,124)
## These are more difficult and may require you to develop faster, more efficient code.
## Hint: you may consider using code for gcd function for greatest common divisor:
## https://www.geeksforgeeks.org/gcd-in-python/

global a # decl a as global var
a = 0 # set a to 0

def egypt(n,d):
    """
    >>> egypt(3,4)
    3/4 = 1/2 + 1/4
    >>> egypt(11,12)
    11/12 = 1/2 + 1/3 + 1/12
    >>> egypt(123,124)
    123/124 = 1/2 + 1/3 + 1/7 + 1/64 + 1/8333 + 1/347186112
    >>> egypt(103,104)
    103/104 = 1/2 + 1/3 + 1/7 + 1/71 + 1/9122 + 1/141449381 + 1/100039636784966424
    """
    
    global a # import a from global scope

    # print out initial n/d = during first run
    if (a == 0):
        print(str(n)+"/"+str(d)+" = ", end="")

    # Calculate iterator / next fraction
    i = (d//n + 1)
    
    if d%n == 0: # ends when denom / numer has no remainder or evenly divides
        print("1/"+str(d//n))
        a=0
        return
    
    # Print out calculated fraction
    print("1/"+str(i)+" + ", end="")
    
    a = 1 # set a to 1
    
    # Use reccursion to calc next fraction
    egypt(n*i-d,d*i)        
        
# Run doctests
import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)
