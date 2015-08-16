import json; 


class Output(object):

	def __init__(self, label):

		self.label = label

		self.fields = []

	def addField(self, field):

		self.fields.append(field)

	def toDict(self):

		ret = {}

		ret['label'] = self.label

		field_dicts = []

		for field in self.fields:

			field_dicts.append(field.toDict())

		ret['fields'] = field_dicts

		return ret



class Field(object):

	def __init__(self, name, value):

		self.name = name;

		self.type = self.outputType(value)


	def outputType(self, sampleValue):

		booleanStrings = ['true', 'false', 'open', 'closed']

		# guess about the type of this output from a sample value
		try:
			# first try numeric
			float(sampleValue)
			return 'numeric'
		except ValueError:

			lowerCaseValue = sampleValue.lower()
			# next try boolean
			for b in booleanStrings:
				if (lowerCaseValue == b):
					return 'boolean'

			return 'string'

	def toDict(self):

		ret = {}

		ret['name'] = self.name

		ret['type'] = self.type

		return ret



class Node(object):

	ROOT_LABEL = 'TreeRootNode'

	def __init__(self, label):

		self.parent = None

		self.children = {}

		self.label = label

		self.value = None


	# add a child
	def addChild(self, newChild):

		newChild.parent = self

		self.children[newChild.label] = newChild

	# get a path back to the root node
	def getPath(self):

		p = self.parent

		ret = [self.label]

		while p.label != Node.ROOT_LABEL:

			ret.append(p.label)

			p = p.parent


		ret = list(reversed(ret))

		return ret

	# get the earliest common ancestor between this 
	# node and any sibling nodes
	def getCommonAncestor(self):

		p = self.parent

		hops = 1

		while len(p.children) == 1:

			p = p.parent

			hops = hops + 1

		return hops

	@staticmethod
	def printTree(rootNode, prefix=''):

		printString = prefix + rootNode.label 

		if rootNode.value:

			printString += ": " + rootNode.value

		print printString

		prefix += '-'

		for child in rootNode.children.keys():

			Node.printTree(rootNode.children[child], prefix)

	@staticmethod
	def newTree():

		return Node(Node.ROOT_LABEL)



class BaseTemplate(object):

	def __init__(self):
		self.outputs = {}

		self.outputTree = Node.newTree()
	
	def createOutputFields(self, data):
		pass


	def toJSON(self):
		outputDicts = []

		for output in self.outputs.values():
			outputDicts.append(output.toDict())


		return json.dumps(outputDicts, indent=4)





