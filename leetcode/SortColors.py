class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count0 = 0
        count1 = 0
        count2 = 0
        for i in range(len(nums)):
            if nums[i]==0:
                count0+=1
            if nums[i]==1:
                count1+=1
            if nums[i]==2:
                count2+=1
        for i in range(len(nums)):
            if i <count0 and count0 >0:
                nums[i]=0
            elif i <count1+count0 and i>=count0 and count1 >0:
                nums[i]=1
            elif i <count2+count0+count1 and i>=count1+count0 and count2 >0:
                nums[i]=2
            print(nums)