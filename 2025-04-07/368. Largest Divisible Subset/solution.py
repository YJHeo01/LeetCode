class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        answer = []
        nums.sort()
        length = len(nums)
        dp = [1] * length
        for i in range(length):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i],dp[j]+1)
        idx = dp.index(max(dp))
        while True:
            answer.append(nums[idx])
            if dp[idx] == 1: break
            for next_idx in range(idx):
                if nums[idx] % nums[next_idx] == 0 and dp[next_idx] == dp[idx] - 1:
                    idx = next_idx
                    break
        return answer
