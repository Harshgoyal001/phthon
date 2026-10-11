'''2778  Sum of Squares of Special Elements 

You are given a 1-indexed integer array nums of length n.

An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.

Return the sum of the squares of all special elements of nums.'''

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            if (len(nums))%(i+1)==0:
                ans += nums[i]*nums[i]

        return(ans)

obj=Solution()
print(obj.sumOfSquares([2,7,1,19,18,3]))