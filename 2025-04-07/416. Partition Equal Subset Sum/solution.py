class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_value = sum(nums)
        if sum_value % 2 == 1: return False
        sum_value //= 2
        dp = [False] * (sum_value+1)
        dp[0] = True
        for num in nums:
            for i in range(sum_value-num,-1,-1):
                if dp[i] == True:
                    dp[i+num] = True
        return dp[sum_value]
