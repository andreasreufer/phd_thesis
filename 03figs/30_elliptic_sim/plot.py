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

sdir = "/Volumes/SSC/c1/mtar000.100_mimp000.010_impa60.0_vimp1.05/"

cfile  = sdir + "clumps_sim.h5part"
d1file = sdir + "dump0006766_T05.0591e-12.h5part"
d2file = sdir + "dump0007316_T02.1912e+03.h5part"
d3file = sdir + "dump0011876_T02.1912e+04.h5part"
d4file = sdir + "dump0044128_T01.0956e+05.h5part"
d5file = sdir + "dump0058443_T01.4155e+05.h5part"

axnorm = [-1.6e10, 1.6e10, -0.9e10, 0.9e10]
axzoom = [-3.2e9 , 3.2e9 , -1.8e9 , 1.8e9 ]
axmed  = [-6.4e9 , 6.4e9 , -3.6e9 , 3.6e9 ]

curcfg = cfg_mat_XY_n
curcfg.xinch = 2.0
curcfg.yinch = 1.0
curcfg.mtar = 0.1
curcfg.mimp = 0.01
curcfg.impa = 60.
curcfg.vimp = 1.05
curcfg.ax = [-6.4e9 , 3.2e9 , -1.6e9 , 3.2e9 ]
curcfg.copy_txt = ""
curcfg.colorFunc = colorBodyAndMatPaper
curcfg.clpr_ls = (0.0, (1,1) )
curcfg.clp_plotsurf = False
curcfg.parm_vc = [0.3, 0.90]
curcfg.filt = "negzonly"
papercolors(curcfg)

curplot = GIplot(cfg_mat_XY_n)
#curplot.doPlot("dump0010797_T01.6386e+04.h5part", "clumps.h5part", "out.png")
curplot.doPlot( d1file, cfile, "out1.png" )
#curplot.doPlot( d2file, cfile, "out2.png" )
#curplot.doPlot( d3file, cfile, "out3.png" )
#curplot.doPlot( d4file, cfile, "out4.png" )
#curplot.doPlot( d5file, cfile, "out5.png" )

