class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # visited = set()

        # def dfs(node, parent):
        #     visited.add(node)

        #     for a, b in edges:
        #         neighbor = None

        #         if a == node:
        #             neighbor = b
                
        #         elif b == node:
        #             neighbor = a

        #         if neighbor is None:
        #             continue
                
        #         if neighbor == parent:
        #             continue
                
        #         if neighbor in visited:
        #             return False
        #         if dfs(neighbor, node) == False:
        #             return False
            
        #     return True
        
        # if dfs(0, -1) == False:
        #     return False
        
        # if len(visited) != n:
        #     return False
        
        # return True




        if len(edges) != n - 1:
            return False
        
        graph = {}
        for node in range(n):
            graph[node] = []
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()

        def dfs(node):
            visited.add(node)

            for neighbor in graph[node]:

                if neighbor in visited:
                    continue
                dfs(neighbor)
        dfs(0)

        if len(visited) == n:
            return True
        
        return False
        


