"""
Leetcode Problem 83
Remove Duplicates
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __repr__(self):
        return self.val
    
class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.val)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        
        # for empty linked list edge case
        if head == None: 
            return head
        
        # parse till end of linked list
        while curr.next is not None: 
            
            # if current value equals next value discard next value
            while curr.val == curr.next.val:
                curr.next = curr.next.next
                
                # if reached end of the list return list
                if curr.next == None: 
                    return head
            
            # set current to next node    
            curr = curr.next
            
            
        return head
        
        
if __name__ == "__main__":
    llist = LinkedList()
    first_node = ListNode(val="a")
    llist.head = first_node
    
    second_node = ListNode(val="b")
    third_node = ListNode(val="c")
    fourth_node = ListNode(val="c")
    fifth_node = ListNode(val="d")
    
    first_node.next = second_node
    second_node.next = third_node
    third_node.next = fourth_node
    fourth_node.next = fifth_node
    
    print(llist)
    
    result = deleteDuplicates(head=llist.head) 
    print(f"Final Answer = {result}")