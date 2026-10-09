from typing import List
class TwoSum:
    def twoSum(self, nums : List[int], target: int) -> List[int]:
        mydict = {}
        for i in range(len(nums)):
            if target - nums[i] in mydict:
                return (i, mydict[target - nums[i]])
            mydict[nums[i]] = i


rel = TwoSum()
a = rel.twoSum([2, 7, 11, 15], 9)
print(a)