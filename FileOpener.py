from ROOT import *
import numpy as np

#Class to open a file using TFile and looks what is inside
def LeafOpener(handle,filename):
	handle = TFile.Open(filename)
	handle.ls()	

	#name = handle.GetClass("TTree").GetName()
	#print(name)






















	#TreeData = handle.GetListOfKeys().GetObjectRef("TTree")
	#print (TreeData)

