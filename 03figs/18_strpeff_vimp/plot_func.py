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

  if msr < 0.01*mimp:# or msr > 0.90*mimp:
    return nan
  else:
    return Arelloss - Brelloss


def filterFunc(sim):
  return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. )

def auxplot(ax):
  pass

#xvar = "vimp"
xvar = "angle"

#yaxis = [ -.30, 1.10 ]
yaxis = [ -1.10, 0.3 ]
ylog  = False
ylbl  = r"$\delta_{SiO_2} - \delta_{Fe}$"
yfmt  = math_formatter
#ytik = (0., 0.5 , 1.0 )  
ytik = (-1.0, -0.5, 0., 0.2)


