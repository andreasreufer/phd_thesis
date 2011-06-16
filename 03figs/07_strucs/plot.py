#!/usr/bin/env python
import numpy as np
import matplotlib as mp
mp.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as col
import matplotlib.mpl    as mpl
import tables as pt

from gi_plot import *
from h5part import H5PartDump
from plot_helpers import *
from const_cgs import *

plt.rc('savefig', dpi=450)


strucA = pt.openFile("strucs_c1/struc_S_00.0010me_S2.40e11_iron0.30_rock0.70_watr0.00.hdf5").root


#ax1 = plt.subplot(222)
ax1 = plt.axes( [0.05, 0.05, 0.3, 0.3])
ax3 = plt.axes( [0.05, 0.35, 0.3, 0.3])
ax2 = plt.axes( [0.35, 0.35, 0.3, 0.3])
ax4 = plt.axes( [0.65, 0.35, 0.3, 0.3])


ax1.plot( strucA.r, strucA.rho, "k-", lw=0.4)
#ax1.axis([0.2, 1.1, 1.9, 13.5])
ax1.set_title(r'$\mathrm{miscible}$')

ax2.plot( strucA.r, strucA.rho, "k-", lw=0.4)
ax3.plot( strucA.r, strucA.p, "k-", lw=0.4)
ax4.plot( strucA.r, strucA.T, "k-", lw=0.4)

#axs = [ax1, ax2, ax3, ax4]
axs = [ax1]
for ax in axs:
  ax.xaxis.set_major_formatter(math_formatter)
  ax.yaxis.set_major_formatter(int_formatter)

plt.savefig("out.pdf")


