"""
Leetcode Problem 2
Add Two Numbers
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

def addTwoNumbersFast(l1,l2): 
    """
    A bit more concise of a solution, avoid try/except block
    Trick is to start with a dummy node and return linked list from
    dummy.next
    """
    p1 = l1
    p2 = l2
    carry = False
    startNode = curr = ListNode(val=0, next=None)
        
    while p1 or p2 or carry: 
            
        if p1 is None:
            add_1 = 0
        else: 
            add_1 = p1.val
            p1 = p1.next
            
        if p2 is None:
            add_2 = 0
        else: 
            add_2 = p2.val
            p2 = p2.next
       
        sum = add_1 + add_2
        
        if carry: 
            sum +=1
        
        carry = False
        
        if sum > 9: 
            sum = sum % 10
            carry = True
        
        curr.next = ListNode(val=sum, next=None)
        curr = curr.next
        
    return startNode.next
  
  
l3 = ListNode(val=3, next=None)      
l2 = ListNode(val=9,next=l3)
l1 = ListNode(val=1,next=l2)

l6 = ListNode(val=2, next=None)      
l5 = ListNode(val=4,next=l6)
l4 = ListNode(val=1,next=l5)

result = addTwoNumbersFast(l1=l1,l2=l4)

print(f"Resulting Linked List is")

while result is not None: 
    print(result.val)
    result = result.next
            
        
