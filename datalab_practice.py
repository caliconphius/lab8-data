# ENGSCI233: Lab - Data
# datalab_practice.py

# PURPOSE:
# To PRACTICE several coding concepts relating to FILE I/O and NETWORK DATA STRUCTURES.

# PREPARATION:
# Notebooks data.ipynb and object_oriented.ipynb

# SUBMISSION:
# DO NOT submit this file. 

# EXERCISE 1: FILE I/O
# In the Data notebook, we saw how a text file could be opened, read, and its contents interpreted in terms of data and
# metadata.

# TO DO:
# - RESEARCH how to use the function np.genfromtxt to read data from 'example_file.txt', returning vectors, xs and Ts.
# - IMPLEMENT this below.

import numpy as np							# this import statement is required to make genfromtxt available


X = np.genfromtxt("example_file.txt", delimiter=",", skip_header=1, )
x, T = X[:,0], X[:,1]
print(x,T)



# EXERCISE 2: NETWORK DATA STRUCTURES
# Networks can be thought of as a series of NODES linked by ARCS.
#
# Each Arc has associated with it a WEIGHT, which could be, say, the capacity of that network connection.
# An Arc points FROM one node TO another, i.e., these are SINGLY DIRECTED Arcs.
#
# Each Node has associated with it a NAME that identifies it, a VALUE (a quantity/location/thing),  
# a list of Arcs ENTERING the node, and a list of Arcs LEAVING the node.

# RATIONALE:
# - We will express each of the concepts above - nodes, arcs, weights, etc. - computationally using 
#   objects, attributes, and methods. 
# - You have been provided pre-prepared scaffolding - a set of partially completed classes and methods
#   in the file datalab_functions.py

# TO DO (PART 1):
# - COMPLETE the add_node() method of the Network class defined in datalab_functions.py
# - How do I know its CORRECT? Test your implementation of the method by PASSING the ASSERT commands below.
# - You DO NOT need to modify any of the commands below.
 
from datalab_functions import*						# make available classes from datalab_functions.py

network = Network()								# create an EMPTY network object
network.add_node('A', 2)						# ADD a new node, name 'A', value 2
ndA = network.get_node('A')						# get the node OBJECT that was created

assert(ndA.name == 'A')							# check its name ATTRIBUTE has been correctly assigned
assert(ndA.value == 2)							# check its value ATTRIBUTE has been correctly assigned

# TO DO (PART 2):
# - COMPLETE the join_nodes() method of the Network class defined in datalab_functions.py
# - How do I know its CORRECT? Test your implementation of the method by PASSING the ASSERT commands below.
# - You DO NOT need to modify any of the commands below.

network.add_node('B', 3)						# ADD a new node, name 'B', value 3
ndB = network.get_node('B')						# get the node OBJECT that was created
network.join_nodes(ndA, ndB, 2)					# JOIN the two nodes in the network

# pay particular attention to which attributes of which objects are being tested below
assert(ndA.arcs_out[0].to_node.name == 'B')		# check node A now POINTS to node B
assert(ndB.arcs_in[0].from_node.name == 'A')    # check node B is POINTED at by node A
assert(ndA.arcs_out[0].weight == 2)             # check WEIGHT has been correctly assigned
assert(len(network.arcs) != 0)                  # check the arc has been ASSOCIATED to the network


# TO DO (PART 3):
# - COMPLETE the read_network() method of the Network class defined in datalab_functions.py
# - How do I know its CORRECT? The display command below should generate the following screen output.
#     A --> B with weight 2
#     A --> C with weight 4
#     B --> C with weight 1
#     B --> D with weight 4
#     C --> D with weight 2
#     C --> E with weight 1
#     D --> E with weight 2
#     D --> F with weight 2
#     E --> F with weight 3
# - You DO NOT need to modify any of the commands below.

network = Network()								# create an EMPTY network object
network.read_network('network.txt')				# READ a network from the file network.txt

network.display()								# PRINT out information about the network
