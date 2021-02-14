import numpy

class KD_TREE:

	def __init__(self, data):
		self.data = data
		self.tree = self.build_tree(leafsize=10)

	def build_tree(self, leafsize=10 ):
		ndim = data.shape[0]
		ndata = data.shape[1]
