class Solution(object):

    def missingRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        input should be in range [0, 99] and should be sorted
        For example, given [0, 1, 3, 50, 99], return ["2", "4->49",]
        """
        if not nums:
            return ['0->99']
        ans = []
        last = len(nums)
        num_should_be = 1
        if nums[0] != 0:
            if nums[0] == 1:
                ans.append("0")
            else:
                ans.append("{}->{}".format(0, nums[0]-1))
                num_should_be = nums[0]+1
        start = 1
        while start < last:
            if nums[start] == nums[start-1]:
                start+=1
                continue
            if nums[start] != num_should_be:
                if num_should_be == nums[start] -1:
                    ans.append("{}".format(num_should_be))
                else:
                    ans.append("{}->{}".format(num_should_be, nums[start]-1))
                num_should_be = nums[start] + 1
            else:
                num_should_be += 1
            start += 1
        if nums[last-1] != 99:
            if nums[last-1] +1 == 99:
                ans.append("{}".format(99))
            else:
                ans.append("{}->{}".format(nums[last-1] +1, 99))
        return ans

arr = [3, 50, 75, 76,77]
obj = Solution()
print obj.missingRanges(arr)
        