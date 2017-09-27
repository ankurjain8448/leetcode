class Solution(object):
	"""
	https://leetcode.com/problems/spiral-matrix
	"""

	def print_row(self, matrix, row, col_start_index, col_end_index, reverse = False):
		arr = matrix[row][col_start_index:col_end_index]
		return arr if not reverse else arr[::-1]

	def print_col(self, matrix, col, row_start_index, row_end_index, reverse = False):
		arr = [ matrix[i][col] for i in xrange(row_start_index, row_end_index)]
		return arr[::-1] if reverse else arr

	def spiralOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		rows = len(matrix)
		ans = []
		if rows == 0:
			return ans
		cols = len(matrix[0])
		x,y = 0,0
		row_start_index = 0 ;row_end_index = rows
		col_start_index = 0 ;col_end_index= cols
		row = 0
		col = 0
		while row_start_index < row_end_index and col_start_index < col_end_index:
			ans.extend(self.print_row(matrix, row, col_start_index, col_end_index))
			ans.extend(self.print_col(matrix, cols - col -1, row_start_index + 1, row_end_index))
			if row != rows - row -1:
				ans.extend(self.print_row(matrix, rows - row -1, col_start_index, col_end_index-1, reverse = True))
			if col != cols - col -1:
				ans.extend(self.print_col(matrix, col, row_start_index + 1, row_end_index - 1, reverse = True))
			row += 1
			col += 1
			row_start_index += 1
			row_end_index -= 1
			col_start_index += 1
			col_end_index -= 1
		return ans
