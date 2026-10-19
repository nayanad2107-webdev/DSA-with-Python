class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        arr=sorted(nums)
        li=[]
        for i in range(len(arr)-2):
            if i>0 and arr[i]==arr[i-1]:
                continue
            tar=arr[i]
            left=i+1
            right=len(arr)-1
            while (left<right):
                sum=arr[left]+arr[right]
                if sum==-tar:
                    li.append([arr[i],arr[left],arr[right]])
                    left+=1
                    right-=1
                    while left<right and arr[left]==arr[left-1]:
                        left+=1
                    while left<right and arr[right]==arr[right+1]:
                        right-=1
                elif sum<-tar:
                    left+=1
                else:
                    right-=1
        return li

                




        