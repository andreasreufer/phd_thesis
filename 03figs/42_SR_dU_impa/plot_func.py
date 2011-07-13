#!/usr/bin/env ipython

from plot_helpers import *
from numpy import sqrt, pi

nan = float('nan')

def plotFunc(sim):
  res = sim.results
  #res.Um[1] -  (res.U0[1] / sim.m)
  u  = res.Um[2] / sim.results.mm[2]
  u0 = res.U0[2] / sim.impb.m
  ret = ( u - u0 ) / u0

  if ret > 0.:
    return ret
  else:
    return nan
  


def filterFunc(sim):
  res = sim.results
  if not sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. ):
    return False

  if not len(sim.results.mm) > 2:
    return False
  
  u  = res.Um[2] / sim.results.mm[2]
  u0 = res.U0[2] / sim.impb.m
  ret = ( u - u0 ) / u0

  if ret < 0.:
    return False

  if not (sim.results.mm[2] > 0.1*sim.impb.m ):
    return False
  else:
    return True


#xvar = "vimp"
xvar = "angle"

yaxis = [  1.e-2, 5.1 ]
ylog  = True 
#ylbl  = r"$\Delta U / E_{imp}$"
ylbl  = r"$\Delta (U / m)_{sr}$"
yfmt  = math_formatter
ytik = ( 0.1, 1., 2., 5.)


