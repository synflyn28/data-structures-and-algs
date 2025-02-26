"""
This script is a solution to the two sum problem.
"""


class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        """
        This method implements the soluton to the two sum problem. It 
        returns the list positions of the two numbers that add up to the
        target number.
        """

        store = {}

        for i in range(len(nums)):
            if nums[i] in store:
                return [store[nums[i]], i]
            else:
                store[target - nums[i]] = i



if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    print(solution.two_sum(nums, target))