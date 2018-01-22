#https://leetcode.com/problems/search-insert-position/description/
class Solution(object):
	def searchInsert(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		start = 0
		end = len(nums) - 1
		s = 0
		e = len(nums)-1
		index = -1
		if target < nums[0]:
			index = 0
		elif target > nums[e]:
			index = e + 1
		else:
			while s <= e:
				mid = (s+e)/2
				if nums[mid] == target:
					index = mid
					break
				elif target < nums[mid]:
					if start < mid and target > nums[mid-1]:
						index = mid
						break
					e = mid - 1
				else:
					if mid < end and target < nums[mid+1]:
						index = mid + 1
						break
					s = mid + 1
		return index
