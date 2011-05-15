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


curcfg = cfg_T___XY_n

curcfg.scal_name = "cost"

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

curcfg.mtar = 0.1
curcfg.mimp = 0.035
curcfg.impa = 30
curcfg.vimp = 2.00
curcfg.scal_min = 2.e-6
curcfg.scal_max = 2.e-5
curcfg.ax = [-6.4e9 , 3.2e9 , -3.2e9 , 1.8e9 ]
curcfg.xinch = 3.2
curcfg.yinch = 2.4
#curcfg.cbar_fmt = '%6.4e'
#curcfg.cbar_fmt = ''
curcfg.cbar_fmt = '%6.4f'
curcfg.cbar_ut = ""
#curcfg.cbar_sc = 7.4e-6
#curcfg.cbar_sc = 2.

#curcfg.filt = "slice"
curplot = GIplot(curcfg)

curplot.doPlot("dump2.h5part", "clumps2.h5part", "out.png")


