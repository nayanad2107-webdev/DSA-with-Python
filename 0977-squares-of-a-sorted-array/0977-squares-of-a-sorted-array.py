class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i=0
        j=k=len(nums)-1
        res=[0]*len(nums)
        while(i<=j):
            left_sq=nums[i]**2
            right_sq=nums[j]**2
            if left_sq>right_sq:
                res[k]=left_sq
                i+=1
                k-=1
            elif left_sq<right_sq:
                res[k]=right_sq
                j-=1
                k-=1
            else:
                res[k]=left_sq
                i+=1
                k-=1
        return res
            

        