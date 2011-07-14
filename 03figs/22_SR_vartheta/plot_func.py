#!/usr/bin/env ipython

from plot_helpers import *
from numpy import sqrt, pi

nan = float('nan')

def plotFunc(sim):
  res = sim.results
  dvinfvec = res.vinfm[2,:] - res.vinfm[1,:]
  dvinf = np.sqrt( (dvinfvec*dvinfvec).sum() )

  #y = (sim.gi.vinf - dvinf) / sim.gi.vesc
  #if y < 0:
  #  y = nan
  #y = dvinf / sim.gi.vesc
  #y = dvinf / sim.gi.vinf
  y = 360.*(res.dblvarthetam[2] - 2.*sim.gi.vartheta)/(2.*pi)
  #y = 360.*(res.dblvarthetam[2])/(2.*pi)
  #y = 360.*(- 2.*sim.gi.vartheta)/(2.*pi)
  #y = (res.dblvarthetam[2] - 2.*sim.gi.vartheta)/( 2.*sim.gi.vartheta )
  #y = (res.dblvarthetam[2])/(2.*sim.gi.vartheta)
  print y, sim.params.key

  return y


def filterFunc(sim, ssname):
  key = sim.params.key
  if ssname == "c1":
    if key == "mtar000.100_mimp000.020_impa60.0_vimp1.10" or \
        key == "mtar000.100_mimp000.020_impa75.0_vimp1.10":
      return False

  return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. ) and (sim.results.mm[2] > 0.1*sim.impb.m and sim.results.dblvarthetam.shape[0] > 2)


#xvar = "vimp"
xvar = "angle"

yaxis = [-65., 20.]
#yaxis = [-10., 10.]
#yaxis = [-3., 1.]
ylog  = False
ylbl  = r"$\Delta \vartheta$"
yfmt  = int_formatter
ytik = (-60., -45., -30., -15., 0., 15.)
#ytik = (-10., 0., 10.)
#ytik = (0.1, 1.)
#ytik = (-2., -1., 0., 1.)
#ytik = (-3., -1., 0, 1.0)


