#file that contains all functions for deltamZ calculation
#---------------------------------------------------------------------------------------------------------

import math as m

#values to lower test calculation
pT1 = 36.8761
pT2 = 36.802
eta1 = 0.511373
eta2 = 1.93236
phi1 = 1.74583
phi2 = -1.37226
massZ = 93.0661

#definition for the magniutde of p, momentum, squared for one lepton
def magp(pT,angle):
	return pT/m.sin(angle)

#definition of the angle theta
def theta(eta):
	return 2*m.atan(m.exp(-eta))

#definition for the angle alpha
def alphaval (phi1,phi2):
	alphap = phi1-phi2 
	if abs(alphap) > m.pi:
		return 2*m.pi - alphap
	else:
		return abs(alphap)

#definition for the invariant mass
def invmass (p1,p2,alpha):
	return m.sqrt(2*p1*p2*(1-m.cos(alpha)))



theta1 = theta(eta1)
theta2 = theta(eta2)

print("theta for l1 is:", theta1,"rad")
print("theta for l2 is:", theta2,"rad")

magp1, magp2 = magp(pT1,theta1), magp(pT2, theta2)

print("the magnitude of l1's momentum is:", magp1, "GeV")
print("the magnitude of l2's momentum is:", magp2, "GeV")

alpha = alphaval(phi1,phi2)

print("value of alpha is:", alpha, "rads")

mZ = invmass(magp1, magp2, alpha)

print("value for the mass of the Z boson is", mZ, "GeV")




