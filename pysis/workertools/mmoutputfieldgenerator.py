from outputfieldtemplate import BaseTemplate
from outputfieldtemplate import Node
from outputfieldtemplate import Output
from outputfieldtemplate import Field
import json


data = [
'Condenser 1st Stage          KEY: master_equip_mcond_stage_0      VALUE: EC1 PUMP',
'Condenser 1st Stage State          KEY: master_equip_mcond_state_0      VALUE: ON',
'Condenser 2nd Stage          KEY: master_equip_mcond_stage_1      VALUE: EC1 FAN 1',
'Condenser 2nd Stage State          KEY: master_equip_mcond_state_1      VALUE: ON']


class MMTemplate(BaseTemplate):

	def __init__(self):
		super(MMTemplate, self).__init__()

	def createOutputFields(self, data):

		for dataPoint in data:

			# grab name and value from this dataPoint
			name = dataPoint.split('KEY:', 1)[0].strip()

			value = dataPoint.split('VALUE:',1)[1].strip()

			# split the name along whitespace
			nameTokens = name.split()

			# build tree
			self.buildTree(self.outputTree, nameTokens, 0, value)

		# make any default fields that need making
		self.makeDefaultFields(self.outputTree)

		# convert the tree to output fields
		self.convertToOutputFields(self.outputTree)

		print self.toJSON()





	def buildTree(self, rootNode, nameTokens, index, value):

		try:

			# check if child exists in dictionary, if not, create it
			# if so, use existing child
			child = None

			if nameTokens[index] in rootNode.children:
				child = rootNode.children[nameTokens[index]]

			else:
				# create child and attach
				child = Node(nameTokens[index])
				rootNode.addChild(child)

			# increment index
			index+=1

			self.buildTree(child, nameTokens, index, value)
		except IndexError:
			# reached end of nameTokens

			# add value to rootNode
			rootNode.value = value
			return

	def makeDefaultFields(self, rootNode):

		# all values must be at the same level of the tree
		# if we find a value, that node has children, we 
		# must create a default field to move the value
		# to the same level of the tree

		childKeys = rootNode.children.keys()

		if rootNode.value:
			# have a value, do we have children?
			if childKeys:
				# have children and a value. give our
				# value to a new child
				newChild = Node("defaultField")

				newChild.value = rootNode.value

				rootNode.addChild(newChild)

				rootNode.value = None

		else:

			for child in childKeys:

				self.makeDefaultFields(rootNode.children[child])


	def convertToOutputFields(self, rootNode):

		childKeys = rootNode.children.keys()

		# we are a leaf node
		if not childKeys:

			# get path back to root from this leaf node
			path = rootNode.getPath()

			# get the number of "hops" up the tree till the first
			# common ancestor
			commonAncestor = rootNode.getCommonAncestor()

			# everything from this number down is the field
			fieldPath = path[-1*commonAncestor:]
			fieldStr = '_'.join(fieldPath)

			# the rest is the output
			outputPath = path[:len(path)-len(fieldPath)]
			outputStr = '_'.join(outputPath)

			# create Output if it doesn't already exist
			output = None

			if outputStr in self.outputs:

				output = self.outputs[outputStr]

			else:

				output = Output(outputStr)

				self.outputs[outputStr] = output


			# create and add field
			field = Field(fieldStr, rootNode.value)
			output.addField(field)




		else:

			# not a leaf node, recurse!
			for childKey in childKeys:

				self.convertToOutputFields(rootNode.children[childKey])






if __name__=='__main__':

    mm = MMTemplate()
    mm.createOutputFields(data)
