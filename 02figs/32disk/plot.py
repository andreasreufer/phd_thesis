#!/usr/bin/env ipython

import matplotlib as mp
mp.use('Agg')
import matplotlib.pyplot as plt

from sim_admin import SimAdmin, SimParam, SimSetConfig
from gi_plot import *
from gi_viz  import GIviz, GIvizConfig
from clumps import ClumpsPlotConfig
import os
import numpy as np

nan = float('nan')

axnorm = [-1.6e10, 1.6e10, -0.9e10, 0.9e10]
axzoom = [-3.2e9 , 3.2e9 , -1.8e9 , 1.8e9 ]

#curcfg = cfg_T___XY_n
curcfg = cfg_orb_XY_m


curcfg.verbose = True
curcfg.T    = 1500

#curcfg.axisbg = "white"
curcfg.plotclmp = False
curcfg.MminLbl = 1.e99
curcfg.copy_txt = ""
curcfg.plotscale = False

#curcfg.scal_min = 5.e-7
#curcfg.scal_max = 2.e-6
#curcfg.ax = [-3.2e9 , 3.2e9 , -1.8e9 , 1.8e9 ]

curcfg.colorFunc = colorOrbit
curcfg.mtar = 1.0
curcfg.mimp = 0.2
curcfg.impa = 32.5
curcfg.vimp = 1.30
#curcfg.scal_min = 0
#curcfg.scal_max = 4
curcfg.ax = [-7.6e9 , 2.0e9 , -4.1e9 , 0.9e9 ]
curcfg.xinch = 3.2
curcfg.yinch = 2.4
#curcfg.cbar_fmt = '%6.4e'
#curcfg.cbar_fmt = ''
curcfg.cbar_fmt = '%6.4f'
curcfg.cbar_ut = ""
curcfg.dmass_vc = [0.7, 0.1] 
#curcfg.cbar_sc = 7.4e-6
#curcfg.cbar_sc = 2.

#curcfg.ax = [-1.2e10,1.2e10 , -5.0e9 , 8.5e9 ]

#curcfg.filt = "slice"
curplot = GIplot(curcfg)
#curplot.doPlot("dump0012740_T02.1345e+03.h5part", "clumps.h5part", "out.png")
#curplot.doPlot("dump0066319_T01.1206e+05.h5part", "clumps.h5part", "out.png")
curplot.doPlot("dump0013961_T01.7315e+04.h5part", "clumps.h5part", "out.png")

