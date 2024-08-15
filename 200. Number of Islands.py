class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #use a queue and hashmap to track already visited
        # queue to track which land needs to be checked next
        # hashmap to determine that this land has already been used in an island 
        # islands = 0, increment every new island 
        landUsed = []
        islands = 0
        n = len(grid)
        m = len(grid[0])

        def determineIsland(row,col):
            queue = [[row,col]]

            while queue:
                cRow,cCol = queue.pop() 
                #print(f"{cRow}{cCol}")
                if cRow+1 < n:  
                    if grid[cRow+1][cCol] == "1": 
                        queue.append([cRow+1,cCol])
                        grid[cRow+1][cCol] = 0
                if cCol+1 < m:
                    if grid[cRow][cCol+1] == "1": 
                        queue.append([cRow,cCol+1])
                        grid[cRow][cCol+1] = 0
                if cRow - 1 >= 0: 
                    if grid[cRow-1][cCol] == "1": 
                        queue.append([cRow-1,cCol])
                        grid[cRow-1][cCol] = 0
                if cCol-1 >= 0:
                    if grid[cRow][cCol-1] == "1": 
                        queue.append([cRow,cCol-1])
                        grid[cRow][cCol-1] = 0
            return None
       
        for row in range(n): 
            for col in range(m): 
                if grid[row][col] == "1":
                    determineIsland(row,col)
                    islands +=1

        return islands
                
