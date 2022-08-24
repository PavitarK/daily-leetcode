"""
Leetcode Problem 509
Fibonacci Number
"""

def fib(n): 
    """
    Approach: Dyanmic programming
    Create a dyanmic array and fill 0-n+1
    return n 
    """   
    
    fib = [0,1]
    
    for i in range(2,n+1): 
        fib.append(fib[i-1]+fib[i-2])
        
    return fib[n]

print(f"Result = {fib(n=5)}")