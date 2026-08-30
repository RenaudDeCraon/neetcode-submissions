class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        i =0
        j = len(nums)
        while(i<j-1):
            if(nums[i] == nums[i+1]):
                return True
            i+=1
        return False


        