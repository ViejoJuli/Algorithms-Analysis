#!/usr/bin/env python3
from collections import Counter
import sys
ans={} #dictionary with character and codification

#Create class node to create Huffman tree.  
class node:
    def __init__(self, freq, character, left=None, right=None):
        # frequency of character
        self.freq = freq
  
        # character name
        self.character = character
  
        # node left of current node
        self.left = left
  
        # node right of current node
        self.right = right
  
        # tree direction (0/1)
        self.direction = ''
  

#Create dictionary with codes from Huffman tree  
def printNodes(node, val=''):
    # huffman code for current node
    newVal = val + str(node.direction)

    #if node is not an edge node then traverse inside it
    if(node.left):
        printNodes(node.left, newVal)
    if(node.right):
        printNodes(node.right, newVal)

    #if node is an edge node then save into answer dictionary
    if(not node.left and not node.right):
        ans[node.character]=newVal
  
  
#Read characters for system string
chars=list(Counter(sys.argv[1]).keys())
freq=list(Counter(sys.argv[1]).values())

#List of unused nodes
nodes = []
  
#Convert characters and frequencies into nodes
for x in range(len(chars)):
    nodes.append(node(freq[x], chars[x]))

while len(nodes) > 1:
    #sort all the nodes in ascending order
    #based on their frequency
    nodes = sorted(nodes, key=lambda x: x.freq)
  
    #pick 2 smallest nodes
    left = nodes[0]
    right = nodes[1]
  
    #assign directional value to these nodes
    left.direction = 0
    right.direction = 1
  
    #combine the 2 smallest nodes to create a new node as their parent
    newNode = node(left.freq+right.freq, left.character+right.character, left, right)
  
    #remove the 2 nodes and add their parent as new node among others
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)

#Huffman Coding
print("Your text is:",len(sys.argv[1])*8,"bits long")
printNodes(nodes[0])
print(ans)
bitstring=""
for char in sys.argv[1]:
    bitstring=bitstring+ans[char]
print(f"The codification for the text is: {bitstring}")
print(f"Now, Your text is now {len(bitstring)} bits long")
