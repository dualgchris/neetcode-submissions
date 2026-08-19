class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        result = []

        for i in range (len(nums)):
            current = nums[i]

            remaining = nums[:i] + nums[i + 1:]

            smaller_perms = self.permute(remaining)

            for perm in smaller_perms:
                result.append([current] + perm)
            
        return result
