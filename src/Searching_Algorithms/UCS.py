#Uniform Cost Search - Made by Aeryes
class GraphNode:
	def __init__(self):
		self.children = []
		self.parents = [] 
		self.cost = 0
		self.value = 0

	def addChild(self, child):
		self.children.append(child)

	def getChildren(self):
		return self.children

	def addParent(self, parent):
		self.parents.append(parent)

	def getParents(self):
		return self.parents

	def setCost(self, cost):
		self.cost = cost

	def getCost(self):
		return self.cost

	def setValue(self, value):
		self.value = value

	def getValue(self):
		return self.value

def UCS(start, goal):
	#Define the frontier.
	frontier = [start]

	#Path taken.
	path = []

	while frontier:
		print("Frotier: ")
		for i in frontier:
			print("Value: " + str(i.getValue()) + " Cost: " + str(i.getValue()))

		#pop the next node.
		current = frontier.pop()
		#Add the current node to the path.
		path.append(current)

		print("Popped: " + str(current.getValue()) + " Cost: " + str(current.getValue()))

		#Check the nodes children and add them to the queue from least cost to highest cost.
		for child in current.getChildren():
			frontier.append(child)

			#Check to see if the current node is the goal.
			if child.getValue() == goal.getValue():
				path.append(child)
				print("\n")
				return child, path
		#Sort the list in descending order.
		frontier.sort(key=lambda x: x.getCost(), reverse = True)
		print("\n")

	return None

def backTrace(path):
	refinedPath = []

	for childIndex in range(len(path)-1):
		if root.getValue() != path[childIndex].getValue():
			if path[childIndex] in path[childIndex+1].getParents():
				refinedPath.append(path[childIndex])

	refinedPath.insert(0, path[0])
	refinedPath.append(path[-1])
	return refinedPath

#Driver Code.
root = GraphNode()
childOne = GraphNode()
childTwo = GraphNode()
childThree = GraphNode()
childFour = GraphNode()
childFive = GraphNode()

root.setValue(0)
root.setCost(0)

childOne.setValue(1)
childOne.setCost(1)
childOne.addParent(root)

childTwo.setValue(2)
childTwo.setCost(2)
childTwo.addParent(root)

childThree.setValue(3)
childThree.setCost(4)
childThree.addParent(childOne)

childFour.setValue(4)
childFour.setCost(1)
childFour.addParent(childTwo)

childFive.setValue(5)
childFive.setCost(1)
childFive.addParent(childThree)
childFive.addParent(childFour)

#Create the graph structure
root.addChild(childOne)
root.addChild(childTwo)
childOne.addChild(childThree)
childTwo.addChild(childFour)
childThree.addChild(childFive)
childFour.addChild(childFive)

#Run UCS on target.
result, path = UCS(root, childFive)

print("Goal returned:" + str(result.getValue()))

#Run the backtrace to find the path.
resultPath = backTrace(path)

minCost = 0
for node in resultPath:
	minCost+=node.getCost()

print("Minimum Cost: " + str(minCost))	
