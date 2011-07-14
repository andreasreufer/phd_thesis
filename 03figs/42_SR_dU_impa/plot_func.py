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
  


def filterFunc(sim, ssname):
  res = sim.results
  if not sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. ):
    return False

  key = sim.params.key
  if ssname == "c1":
    if key == "mtar001.000_mimp000.200_impa60.0_vimp2.50" or \
        key == "mtar000.100_mimp000.020_impa75.0_vimp1.10":
      return False
  if ssname == "i1":
    if key == "mtar000.010_mimp000.002_impa30.0_vimp4.00":
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


