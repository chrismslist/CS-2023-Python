# CS2023 - Lab 3 Required Questions 
# All functions should be written using recursion.
# RQ1


def doubletime(i,n):
    """Returns the result of repeatedly doubling the number i a total of n times
    >>> doubletime(3, 1)
    6
    >>> doubletime(2, 0)
    2
    >>> doubletime(2, 9)
    1024
    """
    
    if n > 0:
        i = i * 2
        n = n - 1
        return doubletime(i,n)
    else:
        return i


# RQ2
def skip2_add(n):
    """ Takes a number x and returns x + x-3 + x-6 + x-9 + ... + 0.

    >>> skip2_add(5)  # 5 + 2  + 0
    7
    >>> skip2_add(10) # 10 + 7 + 4 + 1 + 0
    22
    """
    if n <=0:
        return 0
    return n + skip2_add(n-3)

# RQ3
def a(n):
    """Return the number in the sequence defined by a(1) = 1;
    a(n) = (3/2)*a(n-1) if a(n-1) is even; a(n) = (3/2)*(a(n-1)+1) if a(n-1) is odd.
    (see, http://oeis.org/A070885)

    >>> a(1)
    1
    >>> a(2) 
    3
    >>> a(3)
    6
    >>> a(10)
    123
    """
    
    if (n == 1):
        return 1
    elif (a(n-1) % 2 == 0):
        return int((3/2)*a(n-1))
    elif (a(n-1) % 2 != 0):
        return int((3/2)*(a(n-1)+1))
    else:
        return n
        
    
    
    #return n%(3/2)

#RQ4
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.
    >>> paths(2, 2)
    2
    >>> paths(3, 3)
    6
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    
    Route = []
    b = []
    for i in range(0,m):
        b.append(0)
    
    for j in range(0,n):
        Route.append(b)
    
    
    if( n== 1 or m == 1):
        Route[n-1][m-1] = 1
        return 1
    
    if (Route[n-1][m-1] == 0):
        Route[n-1][m-1] = paths(n-1,m) + paths(n,m-1)
    return Route[n-1][m-1]
    

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)