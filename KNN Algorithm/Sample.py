class Sample:
	distance = 0
	def __init__(self, features, classname = ""):
		self.features = features
		self.classname = classname

	def getClassname(self):
		return self.classname

	def setClassname(self, classname):
		self.classname = classname

	def getDistance(self):
		return self.distance

	def setDistance(self,distance):
		self.distance = distance

	def getFeatures(self):
		return self.features

	def setFeatures(self, features):
		self.features = features

