class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = list()
        nums.sort()
        print (nums)
        for x in range(len(nums)):
            #print nums[x],x
            if x>0 and nums[x]==nums[x-1]:
                continue
            a = nums[x]
            i=x+1
            j=len(nums)-1
            while i<j :
                if a+nums[i]+nums[j]==0 :
                    result.append([a,nums[i],nums[j]])
                    while i<j and nums[i]==nums[i+1]:
                        i=i+1
                    while i<j and nums[j]==nums[j-1]:
                        j=j-1
                    i=i+1
                    j=j-1
                elif a+nums[i]+nums[j]>0 :
                    j=j-1
                    continue
                elif a+nums[i]+nums[j]<0 :
                    i=i+1
                    continue
                   
        return result