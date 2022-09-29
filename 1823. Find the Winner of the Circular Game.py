"""
Leetcode Problem 1823
Find the Winner of the Circular Game
"""

def findTheWinner(n,k):
    circle = [1] * n 
    
    return findTheLoser(circle=circle, start=0, k=k)


def findTheLoser(circle,start,k):
    while friendsLeft(circle) > 1: 
        count = 0
        i = start
        while count < k: 
            if circle[i] == 1: 
                count += 1
            if count !=k: 
                i = findNextStart(circle,i)
        print(circle)
        print(f"i={i}")
        circle[i] = 0
        start = findNextStart(circle,i)
        print(f"next start= {start}")
        print(f"DONE LOOP \n")
    
    return start+1

def findNextStart(circle, i): 
    while True: 
        i = setI(circle, i)
        if circle[i] == 1: 
            return i
        
def setI(circle, i):
    if i == len(circle)-1: 
        i = 0 
    else: 
        i += 1
    #print(f"SET I TO {i}")
    return i 
            

def friendsLeft(circle): 
    count = 0
    for friend in circle: 
        if friend == 1: 
            count += 1
            
    return count

print(f"Friend Left = {findTheWinner(n=10,k=2)}")