from typing import List
class Solution:    
     def twoSum(self, nums: List[int], target: int) -> int:
       n=len(nums)
       for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [nums[i], nums[j]]
       else:
        return 0

# ask the user for input 10 20 30 40 
user_string = input("Enter the Array of numbers (separated by spaces): ")
nums = [int(x) for x in user_string.split()]
target = int(input("Enter the target number: "))
sol = Solution()
output=sol.twoSum(nums, target)
if len(nums) >= 2 and target <= 10e9:
    print("The output is:",output)
else:
    print("num1<=-100 or num2>=100")
