"""
Leetcode Problem 100
Same Tree
"""
"""
Done: 
Runtime: 28 ms, faster than 50.73% of Python online submissions for Same Tree.
Memory Usage: 13.7 MB, less than 12.86% of Python online submissions for Same Tree.
"""

def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    tree1 = []
    tree1 = parseTree(p, tree1)
    tree2 = []
    tree2 = parseTree(q,tree2)
    if tree1 == tree2:
        return True
    
    return False

def parseTree(node, tree): 
    if node == None: 
        return tree
    
    tree.append(node.val)
    
    if node.left: 
        parseTree(node.left,tree)
    else:
        tree.append(None)
        
    if node.right:
        parseTree(node.right, tree)
    else:
        tree.append(None)
        
    return tree