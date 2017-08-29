class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
		n = len(string)
		matrix = [[0 for i in xrange(n)] for j in xrange(n)]

		for i in xrange(n):
			matrix[i][i] = 1

		# start from length 2 to n
		for substring_length in xrange(2, n+1):
			for start_index in xrange(n - substring_length +1):
				end_index = start_index + substring_length - 1
				if string[start_index] == string[end_index] and substring_length == 2:
					matrix[start_index][end_index] = 2
				elif string[start_index] == string[end_index]:
					matrix[start_index][end_index] = matrix[start_index+1][end_index-1] + 2
				else:
					matrix[start_index][end_index] = max(matrix[start_index+1][end_index], matrix[start_index][end_index-1])

		return matrix[0][n-1]
