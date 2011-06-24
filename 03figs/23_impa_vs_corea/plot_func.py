#!/usr/bin/env ipython

from plot_helpers import *
from numpy import sqrt, pi

nan = float('nan')

def plotFunc(sim):
  res = sim.results
  gi  = sim.gi
  tb  = sim.tarb
  ib  = sim.impb

  return y


def filterFunc(sim):
  return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. ) and (sim.results.mm[2] > 0.1*sim.impb.m and sim.results.dblvarthetam.shape[0] > 2)


#xvar = "vimp"
xvar = "angle"

yaxis = [  0., 90.]
#yaxis = [-10., 10.]
#yaxis = [-3., 1.]
ylog  = False
ylbl  = r"$\theta_X [^\circ]$"
yfmt  = int_formatter
ytik = (0., 15., 30., 45., 60., 75., 90.)
#ytik = (-10., 0., 10.)
#ytik = (0.1, 1.)
#ytik = (-2., -1., 0., 1.)
#ytik = (-3., -1., 0, 1.0)


