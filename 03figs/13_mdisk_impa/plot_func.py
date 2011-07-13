#!/usr/bin/env ipython

from plot_helpers import *
from numpy import sqrt, pi

nan = float('nan')

def plotFunc(sim):
  res = sim.results
  #return ( res.mdiskmatm[1,:].sum() / sim.mtot )
  return ( res.mdiskmatm[1,:].sum() / sim.mtot )


def filterFunc(sim):
  res = sim.results
  #return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. ) and (sim.results.mm[2] > 0.1*sim.impb.m )
  return res.valid and ( sim.results.valtmax / sim.tcol > 5. ) and ( res.mdiskmatm[1,:].sum() > 0.001*sim.mtot )


#xvar = "vimp"
xvar = "angle"

yaxis = [  0.9e-4, 0.5 ]
ylog  = True 
ylbl  = r"$M_{disk} / M_{tot}$"
yfmt  = tex_formatter
ytik = ( 0.001, 0.01, 0.1, 1.,)


