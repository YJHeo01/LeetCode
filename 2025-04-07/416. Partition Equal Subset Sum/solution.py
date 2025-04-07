class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_value = sum(nums)
        if sum_value % 2 == 1: return False
        dp = [False] * (sum_value+1)
        dp[0] = True
        for num in nums:
            for i in range(sum_value,-1,-1):
                if dp[i] == True:
                    dp[i+num] = True
        if dp[sum_value//2] == True: return True
        return False
