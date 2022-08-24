"""
Leetcode Problem 94
Binary Tree Inorder Traversal
"""   

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right   

def inOrderTraversal(root):
    """
    'Trivial' recursive solution
    In order traversal: left root right
    --> traverse left tree, root, traverse right tree
    """
    inOrder = []    
    inOrder = builder(root=root, inOrder=inOrder)
    return inOrder
    
    
def builder(root, inOrder):
    """
    helper to build result list
    If root is not None traverse tree
    Else return inOrder as is 
    """ 
    
    if root: 
        builder(root.left, inOrder)
        inOrder.append(root.val)
        builder(root.right, inOrder)
    return inOrder
    
node_1 = TreeNode(val=3, left=None, right=None)
node_2 = TreeNode(val=2, left=None, right=None)
node_3 = TreeNode(val=1,left=node_1, right=node_2)

print(f"Result = {inOrderTraversal(node_3)}")