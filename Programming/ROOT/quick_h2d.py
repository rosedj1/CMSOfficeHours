import ROOT as rt
import numpy as np   

x_vals = np.random.normal(5, 3, 10000)
y_vals_1 = np.random.normal(7, 2, 10000) 
y_vals_2 = np.random.normal(2, 1, 10000)

h2 = rt.TH2F("h2", "#bf{#it{#Blessed}}, baby;Percent chance of success (%);Dice pool",  
10, 0, 10, 
5, 2, 7)

for x,y1,y2 in zip(x_vals, y_vals_1, y_vals_2): 
    h2.Fill(x,y1,1) 
    h2.Fill(x,y2,1) 

c1 = rt.TCanvas()
h2.Draw("colz text")
c1.Update()

h2.SetContour(200)
