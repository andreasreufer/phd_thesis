#!/usr/bin/env ipython

from plot_helpers import *
from numpy import sqrt, pi

nan = float('nan')

def plotFunc(sim):
  res = sim.results
  
  matA = 1
  matB = 5

  Arelloss = -( sim.impb.mmat[matA] - res.mmatm[2,matA] ) / sim.impb.mmat[matA]
  Brelloss = -( sim.impb.mmat[matB] - res.mmatm[2,matB] ) / sim.impb.mmat[matB]
  
  msr  = res.mm[2]
  mimp = sim.impb.m

  return (Brelloss - Arelloss)


def filterFunc(sim):
  res = sim.results
  if not ( sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. ) ):
    return False

  if not res.mmatm.shape[0] > 2:
    return False

  if res.mm[2] > 0.05*sim.impb.m:
    return True
  else:
    return False


def auxplot(ax):
  pass

#xvar = "vimp"
xvar = "angle"

#yaxis = [ -.30, 1.10 ]
yaxis = [ -0.1, 1.10 ]
ylog  = False
ylbl  = r"$\delta_{SiO_2} - \delta_{Fe}$"
yfmt  = math_formatter
#ytik = (0., 0.5 , 1.0 )  
ytik = (0.0, 0.25, 0.5, 0.75, 1.0 )


