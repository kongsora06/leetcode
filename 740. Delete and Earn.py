# You are given an integer array nums. You want to maximize the number of 
# points you get by performing the following operation any number of times:

# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you 
# must delete every element equal to nums[i] - 1 and every element equal 
# to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above 
# operation some number of times.

# Example 1:
# Input: nums = [3,4,2]
# Output: 6
# Explanation: You can perform the following operations:
# - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
# - Delete 2 to earn 2 points. nums = [].
# You earn a total of 6 points.

# Example 2:
# Input: nums = [2,2,3,3,3,4]
# Output: 9
# Explanation: You can perform the following operations:
# - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
# - Delete a 3 again to earn 3 points. nums = [3].
# - Delete a 3 once more to earn 3 points. nums = [].
# You earn a total of 9 points.

from collections import Counter
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        count = Counter(nums)
        max_num = max(nums)

        dp0, dp1 = 0, count[1] * 1
        for i in range(2, max_num + 1):
            points = count[i] * i   # calculated the points
            current = max(dp1, dp0 + points)    # find the max amount
            dp0, dp1 = dp1, current # shift one space ahead
        return dp1  # the bigger number shifts to dp1
            
# test cases 
sol = Solution()
print(sol.deleteAndEarn([3,4,2]))
print(sol.deleteAndEarn([2,2,3,3,3,4]))