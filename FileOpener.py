from ROOT import *
import numpy as np

#Class to open a file using TFile and looks what is inside
def LeafOpener(function):
	return function**2

y = LeafOpener(2)
print (y)	
