# The Tribonacci sequence Tn is defined as follows: 
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.

# Example 1:
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4

# Example 2:
# Input: n = 25
# Output: 1389537

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        num1 = 0
        num2 = 1
        num3 = 1
        sol = 0
        if(n == 1):
            return 1
        elif(n == 2):
            return 1
        else:
            while(count < n - 2):
                sol = num1 + num2 + num3
                num1 = num2
                num2 = num3
                num3 = sol
                count += 1
            return sol

# test cases
sol = Solution()
print(sol.tribonacci(4)) # Expected output: 4
print(sol.tribonacci(25)) # Expected output: 1389537