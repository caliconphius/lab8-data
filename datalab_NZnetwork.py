# ENGSCI233: Lab - Data
# datalab_NZnetwork.py

# PREPARATION:
# Complete the activities in datalab_practice.py.

# SUBMISSION:
# DO NOT submit this file. 

# EXERCISE: The NZ electricity network
# In this task, you will work on the derived class NetworkNZ.
# - A DERIVED class uses another class as a template and makes modifications.
# - In this case, the Network class is the template, and we are modifying the read_network() method.
# - All other methods and attributes are the same as the Network class.

# TO DO:
# - DOWNLOAD and UNZIP the file nz_network.zip, which contains files summarising the NZ electricity network.
# - COMPLETE the read_network() method of the NetworkNZ class defined in datalab_functions.py. 
#   Read the NOTES in the docstring for this method to understand how it should work.
# - RUN the commands below to generate a plot of the NZ electricity network. 
# - How do I know its CORRECT? The plot you generate should match up with the one in the lab document.

from datalab_functions import*						# make available classes from datalab_functions.py

nz = NetworkNZ()								# create an EMPTY NZ network object
nz.read_network('nz_network')					# READ a network from the FOLDER nz_network

nz.show(save='datalab_network.png')							# CREATE a plot of the network


# Some SUGGESTIONS if you're getting a bit stuck.
# - Take a look at the folder structure of nz_network. Sketch the files and folders for a couple of stations.
# - If you were to represent this as a Network objects, what would be the nodes? The arcs? The weights and
#   values? Sketch these for a couple of stations.
# - If you had to construct the network by hand, write down a methodical list of steps to navigate the
#   folders, get the relevant information, and assign it to the various objects.
# - For the steps you have written, tag them with methods or attributes that you have previously used.
# - Write this down as a series of PSEUDOCODE steps inside of read_network().
# - What command do we use to return an unknown set of files and folders conforming to a particular string
#   pattern?
# - Make sure to convert the station locations from strings to floats.
