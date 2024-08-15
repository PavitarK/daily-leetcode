class Solution:
    count = 0
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # consider this a graph problem 
        # take capital as the root
        # create an adjacency list 
        # hashmap: node : [adjacent nodes]

        adj = []
        for i in range(n): 
            adj.append([])
        
        for i in connections:
            # add the real and fake connections
            # ie) going from start to dest is a true connection
            # the reverse is a fake connection
            adj[i[0]].append([i[1],1]) 
            adj[i[1]].append([i[0],0])
                 
        def dfs(child, parent): 
            #LIFO --> stack 
            for [c,d] in adj[child]: 
                if c != parent: 
                    self.count+=d
                    dfs(c,child)

        dfs(0,-1) 
        return self.count