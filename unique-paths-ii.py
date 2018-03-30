class Solution(object):
	def uniquePathsWithObstacles(self, obstacleGrid):
		"""
		:type obstacleGrid: List[List[int]]
		:rtype: int
		"""
		rows = len(obstacleGrid)
		cols = len(obstacleGrid[0])
		# arr = [ [1 for i in xrange(cols)] for j in xrange(rows)]
		for i in xrange(cols):
			if obstacleGrid[0][i] == 1:
				for j in xrange(i, cols):
					obstacleGrid[0][j] = 0
				break
			else:
				obstacleGrid[0][i] = 1
		for i in xrange(rows):
			if obstacleGrid[i][0] == 1:
				for j in xrange(i, rows):
					obstacleGrid[j][0] = 0
				break
			else:
				obstacleGrid[i][0] = 1
		for i in xrange(1,rows):
			for j in xrange(1,cols):
				if obstacleGrid[i][j] == 1:
					obstacleGrid[i][j] = 0
				else:
					obstacleGrid[i][j] = obstacleGrid[i][j-1] + obstacleGrid[i-1][j]
		return obstacleGrid[rows-1][cols-1]

