class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        visited = set()

        def dfs(node, parent):
            visited.add(node)

            for a, b in edges:
                neighbor = None

                if a == node:
                    neighbor = b
                
                elif b == node:
                    neighbor = a

                if neighbor is None:
                    continue
                
                if neighbor == parent:
                    continue
                
                if neighbor in visited:
                    return False
                if dfs(neighbor, node) == False:
                    return False
            
            return True
        
        if dfs(0, -1) == False:
            return False
        
        if len(visited) != n:
            return False
        
        return True