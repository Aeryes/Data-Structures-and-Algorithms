#Breadth First Search
#If you want to find the path to a target, one method that offers more control that just
#defining a predessor node function is to create a Node class.This way you can track the 
#parent and children nodes using class variables and use this information to perform a simple back trace to find
#the path to your desired target. You can also use the class for other functions, such as defining a board for a
#game such as 8-Puzzle or N-Queens.
from collections import deque

def bfs(graph, start):
	#Create the frontier.
	frontier = deque([start])

	#List to store nodes that have already been visited.
	visitedNodes = []

	while frontier:
		#Pop and get current node.
		currentNode = frontier.pop()

		#Add the current node to the visited nodes list.
		visitedNodes.append(currentNode)

		#Get the children of the current node and add them to the frontier.
		for child in graph[currentNode]:
			if child not in visitedNodes:
				frontier.appendleft(child)

	return visitedNodes

#Driver code.
testGraph = {
'0':('3','5','9'),
'1':('6','7','4'),
'2':('10','5'),
'3':('0'),
'4':('1','5','9'),
'5':('2','8','4'),
'6':('1'),
'7':('1'),
'8':('4'),
'9':('0'),
'10':('2')}

print(bfs(testGraph, '0'))