#!/usr/bin/env ipython

from plot_helpers import *
from numpy import sqrt, pi

nan = float('nan')

def plotFunc(sim):
  res = sim.results
  #res.Um[1] -  (res.U0[1] / sim.m)
  u  = res.Um[1] / sim.results.mm[1]
  u0 = res.U0[1] / sim.tarb.m
  
  #return (res.Um[1] - res.U0[1]) / sim.gi.Ered
  return ( u - u0 ) / u0


def filterFunc(sim):
  #return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. ) and (sim.results.mm[2] > 0.1*sim.impb.m )
  return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. )


#xvar = "vimp"
xvar = "angle"

yaxis = [  1.e-2, 5.1 ]
ylog  = True 
#ylbl  = r"$\Delta U / E_{imp}$"
ylbl  = r"$\Delta (U / m)_{lr}$"
yfmt  = math_formatter
ytik = ( 0.1, 1., 2., 5.)


