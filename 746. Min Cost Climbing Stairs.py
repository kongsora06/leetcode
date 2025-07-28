# You are given an integer array cost where cost[i] is the cost of ith step 
# on a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

# Example 1:
# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.

# Example 2:
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp1 = 0
        dp2 = 0
        if(len(cost) == 1):
            return cost[0]
        else:
            for i in range(2, len(cost) + 1):
                current = min(dp2 + cost[i - 1], dp1 + cost[i - 2])
                dp1, dp2 = dp2, current
            return dp2
        
# test cases
sol = Solution()
print(sol.minCostClimbingStairs([10,15,20])) # Expected output: 15
print(sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])) # Expected output: 6