#!/usr/bin/env ipython

from plot_helpers import *
from numpy import sqrt, pi

nan = float('nan')

def plotFunc(sim):
  res = sim.results
  return (res.Epotm[1] - res.Epot0[1] - res.Epot0[2]) / sim.gi.Ered


def filterFunc(sim, ssname):
  #return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. ) and (sim.results.mm[2] > 0.1*sim.impb.m )

  key = sim.params.key
  if ssname == "c1":
    if key == "mtar001.000_mimp000.700_impa00.1_vimp1.00" or \
        key == "mtar001.000_mimp000.700_impa52.5_vimp1.00" or \
        key == "mtar001.000_mimp000.700_impa89.0_vimp1.00" or \
        key == "mtar001.000_mimp000.700_impa60.0_vimp1.40" or \
        key == "mtar001.000_mimp000.700_impa30.0_vimp1.60" or \
        key == "mtar001.000_mimp000.700_impa75.0_vimp1.10" or \
        key == "mtar001.000_mimp000.700_impa45.0_vimp1.15" or \
        key == "mtar001.000_mimp000.700_impa45.0_vimp1.05" or \
        key == "mtar000.010_mimp000.002_impa60.0_vimp1.20" or \
        key == "mtar000.100_mimp000.020_impa75.0_vimp1.10" or \
        key == "mtar001.000_mimp000.700_impa75.0_vimp1.00":
          return False
    

  return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. ) and ( sim.results.Epot0.shape[0] > 2 )


#xvar = "vimp"
xvar = "angle"

yaxis = [-1.7, 1.7]
ylog  = False
#ylbl  = r"$E_{pot, lr} - E_{pot, targ} - E_{pot, imp}$"
ylbl  = r"$\Delta E_{pot} / E_{imp}$"
yfmt  = math_formatter
ytik = ( -1., 0., 1.0)


