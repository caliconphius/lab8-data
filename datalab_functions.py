# ENGSCI233: Lab - Data
# datalab_functions.py

# PURPOSE:
# To IMPLEMENT several METHODS for NETWORK DATA STRUCTURES.

# SUBMISSION:
# - YOU MUST submit this file to complete the lab.
# - DO NOT change the file name.

# TO DO:
# - COMPLETE the methods add_node(), join_nodes() and read_network() as part of the Network class.
# - COMPLETE the method read_network() as part of the NetworkNZ class.
# - DO NOT modify the other classes and methods.

# imports
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from glob import glob


# these classes and methods are complete, do not modify them
class Node(object):
    """ Object representing network node.

        Attributes:
        -----------
        name : str, int
            unique identifier for the node
        value : any type
            information associated with the node (could be float, int, bool, str, list, etc)
        arcs_in : list
            Arc objects that end at this node
        arcs_out : list
            Arc objects that begin at this node
    """
    def __init__(self):
        self.name = None
        self.value = None
        self.arcs_in = []
        self.arcs_out = []

    def __repr__(self):
        return f"nd:{self.name}"


class Arc(object):
    """ Object representing network arc.

        Attributes:
        -----------
        weight : flaot
            information associated with the arc
        to_node : Node
            Node object (defined above) at which arc ends.
        from_node : Node
            Node object at which arc begins.
    """
    def __init__(self):
        self.weight=None
        self.to_node = None
        self.from_node = None

    def __repr__(self):
        return f"({self.from_node.name})-->({self.to_node.name})"


class NetworkError(Exception):
    """ An error to raise when violations occur.
    """
    pass


# **this class is incomplete, you must complete it as part of the lab task**
#                 ----------
class Network(object):
    """ Basic network class.
    """
    # these methods are complete, do not modify them
    def __init__(self):
        self.nodes = []
        self.arcs = []

    def __repr__(self):
        return 'ntwk'

    def get_node(self, name):
        """ Return network node with name.

            Parameters:
            -----------
            name : str
                name of node to return

            Returns:
            --------
            nd : Node
                Node object (defined above) with corresponding name.

            Raises:
            -------
            NetworkError : If node does not exist.
        """
        # loop through list of nodes until node found
        for node in self.nodes:
            if node.name == name:
                return node
        # only gets here if failed to find node
        raise NetworkError

    def display(self):
        """ Prints information about the network.
        """
        # get names of nodes
        node_names = ','.join(nd.name for nd in self.nodes)
        # print nodes
        print(f"network has {len(self.nodes)} nodes: {node_names}")
        # print arcs
        for arc in self.arcs:
            print(f"{arc.from_node.name} --> {arc.to_node.name} with weight {arc.weight}")

    # **these methods are incomplete, you must complete them as part of the lab task**
    def add_node(self, name, value=None):
        """ Adds a Node with NAME and VALUE to the network.

            parameters
            ----------
            name : str
                Name of the node being added to the network
            value : any type
                Value of the node being added to the network
        """

        # **to do: create an empty node object, assign its attributes**
        # **hint 1: how is an empty network object created in datalab_practice.py?**
        # **hint 2: take a look Section 0.6 in python101.ipynb, particularly attribute assignment**
        # **hint 3: what values do the method arguments NAME and VALUE take when the add_node method
        #           is called in datalab_practice.py?**
        # **hint 4: what does the input argument 'self' represent in this method?**

        # 1. WRITE PSEUDOCODE BELOW (optional, recommended)
        # **your pseudocode here**

        # 2. IMPLEMENT COMMANDS FOR YOUR PSEUDOCODE
        # ___
        node = Node()
        node.name = name
        node.value = value     # replace this command

        # 3. THINK VERY CAREFULLY ABOUT WHAT THE NEXT COMMAND IS DOING
        # append node to the list of nodes
        self.nodes.append(node)

    def join_nodes(self, node_from, node_to, weight):
        """ Adds an Arc joining NODE_FROM to NODE_TO with WEIGHT.

            node_from : node
                node the arc is going from
            node_to : node 
                node the arc is going to
            weight : any type
                weight of the arc
        """
        # **to do: create an empty arc object, assign its attributes**
        # **hint: both input nodes have lists called arcs_in and arcs_out.
        # **   - what information do these store?
        # **   - because they are lists, they can be modified using the append method

        # 1. WRITE PSEUDOCODE BELOW (optional, recommended)
        # ___

        # 2. IMPLEMENT COMMANDS FOR YOUR PSEUDOCODE
        # ___
        arc = Arc()
        arc.weight = weight
        arc.to_node = node_to
        arc.from_node = node_from

        node_to.arcs_in.append(arc)
        node_from.arcs_out.append(arc)

        self.arcs.append(arc)

    def read_network(self, filename):
        """ Read data from FILENAME and construct the network.

            Each line of FILENAME contains
             - the name of an origin node (first entry)
             - and destination;weight pairs (each pair separated by a comma)

        """
        # **to do**
        # **hint: inspect 'network.txt' so that you understand the file structure**
        # **hint: each source-destination node pair needs to be joined

        # THE PSEUDOCODE FOR THIS METHOD HAS ALREADY BEEN WRITTEN BELOW

        # open the file
        # the 'with' construct automagically manages closing the file
        with open(filename, 'r') as fp:
            
            # loop over the lines of the file
            for line in fp:
                # - strip() is a useful method that removes white-space from the 
                # beginning and end of the string
                ln = line.strip()

                # divide the string using the split() method for strings
                # - extract the source node
                # - extract the remaining arcs
                node_list = ln.split(",")
                
        
                # YOU WILL NEED TO THINK CAREFULLY ABOUT WHAT THIS TRY/EXCEPT BLOCK DOES
                # if node doesn't exist, add to network
                try:
                    # the output is a node object, the input is a string
                    # this command raises an ERROR if the node DOESN'T exist
                    source_name = node_list.pop(0)
                    source_node = self.get_node(source_name)
                except NetworkError:
                    # this command gets executed if an error is raised above
                    self.add_node(source_name)

                    # get the source node OBJECT, using the source node STRING
                    source_node = self.get_node(source_name)

                # read the arc information and add it to network
                for item in node_list:
                    # parse arc information
                    info = item.split(";")  
                    self.add_node(info[0])
                    new_node = self.get_node(info[0])

                    # get destination node object and link it to source node
                    self.join_nodes(source_node, new_node, info[1])

       
                    


# **this class is incomplete, you must complete it as part of the lab task**
#                 ----------
class NetworkNZ(Network):
    """ Derived Network class, for NZ networks.
    """

    # **this method is incomplete, you must complete it as part of the lab**
    def read_network(self, directory):
        """ Reads network information from input string DIRECTORY

            Notes:
            ------
            Assume that DIRECTORY contains one folder for connections between nodes.
            All other folders define the nodes of the network.

            Each node folder contains a file called station_data.txt
            This file includes the node name and x and y values for the node position.

            In the connections folder, there is a file for each connection.
            The name of the file indicates that two nodes are connected (from-to).
            The contents of the file record the capacity of that connection over the last 35 years.
            The connection (arc) weight should be the mean capacity.

            DO NOT HARD CODE the directory path. This is received through the 'directory' argument.
        """

        # **some useful functions**
        # glob
        # np.genfromtxt
        # os.path.isdir
        # ___

        # **delete the placeholder command below once you have written your code**
        pass

    # this method is complete, do not modify
    def show(self, save=None):
        """ Plot the network and optionally save to file SAVE
        """
        # create figure axes
        fig = plt.figure()
        fig.set_size_inches([10, 10])
        ax = plt.axes()

        # NZ coastline as background
        img = mpimg.imread('bg.png')
        ax.imshow(img, zorder=1)

        # a filthy hack to get coordinates in the right spot...
        for node in self.nodes:
            try:
                modified = node._modified
            except AttributeError:
                x, y = node.value
                y = int((y+10)*1.06)
                x -= int(50*y/800.)
                node.value = [x, y]
                node._modified = True

        # draw nodes as text boxes with station names
            # bounding box properties
        props = dict(boxstyle='round', facecolor='white', alpha=1.0)
        for node in self.nodes:
            # extract coordinates
            x, y = node.value
            ax.text(x, y, node.name, ha='center', va='center', zorder=2, bbox=props)

        try:
            md = {'a': os.environ['COMPUTERNAME']}
        except KeyError:
            try:
                import socket
                md = {'a': socket.gethostname()}
            except:
                md = None
                pass

        # draw connections as lines
        weights = [arc.weight for arc in self.arcs]
        # scale for plotting connections
        wmin = np.min(weights)
        wmax = np.max(weights)
        lmin, lmax = [0.5, 10.0]

        # plot connections
        for arc in self.arcs:
            # compute line length, scales with connection size
            lw = (arc.weight-wmin)/(wmax-wmin)*(lmax-lmin)+lmin
            x1, y1 = arc.from_node.value
            x2, y2 = arc.to_node.value
            ax.plot([x1, x2], [y1, y2], '-', lw=lw, color=[0.6, 0.6, 0.6])

        # remove ticks
        ax.set_xticks([])
        ax.set_yticks([])

        # display options
        if save:

            # save to file
            plt.savefig(save, dpi=300, facecolor='w', edgecolor='w', orientation='portrait', papertype=None,
                        format=None, transparent=False, bbox_inches=None, pad_inches=0.1, frameon=None,  metadata=md)
            plt.close()
        else:
            # open figure window in screen
            plt.show()
