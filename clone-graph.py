# Definition for a undirected graph node
# class UndirectedGraphNode:
#	 def __init__(self, x):
#		 self.label = x
#		 self.neighbors = []

class Solution:
	# @param node, a undirected graph node
	# @return a undirected graph node
	def dfs(self, node):
		if node in self.visited_nodes:
			return self.visited_nodes[node]
		new_node = UndirectedGraphNode(node.label)
		self.visited_nodes[node] = new_node
		for each_neighbour in node.neighbors:
			new_node.neighbors.append(self.dfs(each_neighbour))
		return new_node

	def cloneGraph(self, node):
		if node is None:
			return node
		self.visited_nodes = {}
		return self.dfs(node)
