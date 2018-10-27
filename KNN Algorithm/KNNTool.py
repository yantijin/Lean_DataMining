from Sample import *
from math import pow
class KNNTool:
	calssWeightArray = [1,1,1,1]
	testDataPath = ""
	trainDataPath = ""
	classTypes = []
	resultSamples = []
	trainSamples = []
	trainData = []
	testData = []

	def __init__(self,trainDataPath, testData):
		self.trainDataPath = trainDataPath
		self.testDataPath = testData
		self.radDataFromFile()

	def fileDataToArray(self, filePath):
		file_obj = open(filePath)
		data = []
		data1 = []
		try:
			for line in file_obj.readlines():

				tmp = line.replace("\n","").split(' ')
				tmplen = len(tmp)
				for nm in range(tmplen):
					data1.append(tmp[nm])
				data.append(data1)
				data1 = []
		finally:
			file_obj.close()

		return data

	def radDataFromFile(self):
		self.trainData = self.fileDataToArray(self.trainDataPath)
		for s in self.trainData:
			if s[0] not in self.classTypes:
				self.classTypes.append(s[0])

		self.testData = self.fileDataToArray(self.testDataPath)
		# print("testData")
		print(self.testData)
		print(self.trainData)

	def computeDistance(self, s1, s2):
		f1 = s1.getFeatures()
		f2 = s2.getFeatures()
		distance = 0
		for i in range(len(f1)):
			subF1 = int(f1[i])
			subF2 = int(f2[i])
			distance += pow((subF1-subF2),2)
		return distance

	def knnCompute(self, k):
		tempF = None
		classCount = {}
		classWeight = {}

		for s in self.testData:
			temp = Sample(s)
			self.resultSamples.append(temp)


		for s in self.trainData:
			className = s[0]
			# print(s[1:])
			temp = Sample(s[1:], className)
			self.trainSamples.append(temp)

		KNNSample = []

		for s in self.resultSamples:
			classCount = {}
			index = 0
			for type in self.classTypes:
				classCount[type] = 0
				classWeight[type] = self.calssWeightArray[index]
				index += 1
			# print("classcount:{0}".format(classCount))

			for ts in self.trainSamples:

				dis = self.computeDistance(s, ts)
				ts.setDistance(dis)

			lp = sorted(self.trainSamples, key = lambda sample:sample.getDistance())
			self.trainSamples = lp
			KNNSample = []

			for i in range(len(self.trainSamples)):
				if i<k:
					KNNSample.append(self.trainSamples[i])
				else:
					break

			for s1 in KNNSample:
				# print(s1.getClassname())
				num = classCount[s1.getClassname()]
				num += classWeight[s1.getClassname()]
				classCount[s1.getClassname()] = num

			maxCount = 0




			for ss in classCount:
				if int(classCount[ss]) > maxCount:
					maxCount = int(classCount[ss])
					s.setClassname(ss)

			print("测试数据特征：")
			for s1 in s.getFeatures():
				print("%s " % s1,end="")

			print("分类： %s" % s.getClassname())


if __name__ =="__main__":
	trainDataPath = "trainInput.txt"
	testDataPath = "testInput.txt"
	tool = KNNTool(trainDataPath, testDataPath)
	tool.knnCompute(3)







