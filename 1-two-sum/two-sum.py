class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        notebook = {}                      # number -> spot where I saw it

        for spot, num in enumerate(nums):
            friend = target - num          # the friend I need
            if friend in notebook:         # is my friend in the notebook?
                return [notebook[friend], spot]
            notebook[num] = spot           # no? write myself down

        