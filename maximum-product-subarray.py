nums = [2,3,-2,4]
n = len(nums)
if n == 0:
	return 0
i = 0
# while i < n and nums[i] < 0:
# 	i += 1

temp = 1
ans = 1
final_ans = 1
while i < n:
	val = nums[i]
	if val < 0:
		temp = temp*val
	elif val > 0:
		ans = ans*val
	else:
		pass
	i+=1