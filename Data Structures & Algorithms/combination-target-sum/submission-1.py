class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        combination = []
        output = []
        
        def dfs(i, total):
            if total == target:
                output.append(combination.copy())
                return
            
            if total > target or i == len(nums):
                return
            
            combination.append(nums[i])
            total += nums[i]

            dfs(i, total)

            combination.pop()
            total -= nums[i]

            dfs(i+1, total)
        
        dfs(0, 0)

        return output
            