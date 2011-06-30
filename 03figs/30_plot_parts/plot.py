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
axmed  = [-6.4e9 , 6.4e9 , -3.6e9 , 3.6e9 ]

curcfg = cfg_mat_XY_n
curcfg.mtar = 1.0
curcfg.mimp = 0.1
curcfg.impa = 30.
curcfg.vimp = 2.0
curcfg.ax = axmed
curcfg.copy_txt = ""
curcfg.colorFunc = colorBodyAndMatPaper
papercolors(curcfg)

curplot = GIplot(cfg_mat_XY_n)
curplot.doPlot("dump0010797_T01.6386e+04.h5part", "clumps.h5part", "out.png")

