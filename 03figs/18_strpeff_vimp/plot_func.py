#!/usr/bin/env ipython

from plot_helpers import *
from numpy import sqrt, pi

nan = float('nan')

def plotFunc(sim):
  res = sim.results
  #return (res.mm[1] - sim.tarb.m) / sim.impb.m
  #accreff = (res.mm[1] - sim.tarb.m) / sim.impb.m
  #strpeff = (sim.impb.m - res.mm[2]) / sim.impb.m

  #mat = 1
  mat = 5

  matA = 1
  matB = 5

  Arelloss = ( sim.impb.mmat[matA] - res.mmatm[2,matA] ) / sim.impb.mmat[matA]
  Brelloss = ( sim.impb.mmat[matB] - res.mmatm[2,matB] ) / sim.impb.mmat[matB]
  
  msr  = res.mm[2]
  mimp = sim.impb.m

  if msr < 0.01*mimp or msr > 0.90*mimp:
    return nan
  else:
    return Arelloss - Brelloss

  mimpmat = sim.impb.mmat[mat]
  
  frac = res.mmatm[2,mat] / res.mm[2]
  frc0 = sim.impb.mmat[mat] / sim.impb.m

  

  #if res.mm[2] < 0.1*sim.impb.m:
  if msr < 0.1*mimp or msr > 0.90*mimp:
    return nan
  else:
    return frac
    #return  res.mmatm[2,mat] / sim.impb.mmat[mat]

  dfrc = (frac - frc0) / frc0

  if res.mm[2] < 0.1*sim.impb.m:
    dfrc = nan
  return dfrc

def filterFunc(sim):
  #return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. ) and (sim.results.mm[2] > 0.1*sim.impb.m )
  return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. )

def auxplot(ax):
  pass

#xvar = "vimp"
xvar = "angle"

yaxis = [ -0.1, 1.0 ]
ylog  = False
ylbl  = r"$\xi$"
yfmt  = math_formatter
ytik = (0., 0.5 , 1.0 )  


