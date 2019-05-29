from ROOT import *
def FileOpen(f, filename):
        f = TFile.Open(filename)
        f.ls()
