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

plt.rc('savefig', dpi=300)

dumpMf = H5PartDump("misc/body_S_00.903me_S3.50e11_iron0.30_rock0.70_watr0.00_885k.h5part")
dumpM = dumpMf.getStepFirst()

dumpSf = H5PartDump("stnd/body_S_00.903me_S3.50e11_iron0.30_rock0.70_watr0.00_885k.h5part")
dumpS = dumpSf.getStepFirst()

prof = pt.openFile("struc_S_00.903me_S3.50e11_iron0.30_rock0.70_watr0.00.hdf5").root

def getPoints(dump):
  filt = ( -2.e7 < dump.pos[:,2] ) & ( 2.e7 > dump.pos[:,2] )

  rvec = dump.pos[:,:].compress(filt, axis=0)[:,:]
  r   = np.sqrt( (rvec*rvec).sum(axis=1) )

  rho = dump.rho[:,0].compress(filt)[:]
  p   = dump.p[:,0].compress(filt)[:]
  mat = dump.mat[:,0].compress(filt)[:]

  cmap = np.zeros((2,6,3))
  cmap[0,1] = cnameToRGB("red")
  cmap[0,5] = cnameToRGB("mediumblue")

  col = cmap[0, mat] 
  return (r, rho, p, col)

(rM, rhoM, pM, colM) = getPoints(dumpM)
ax1 = plt.subplot(222)
ax1.scatter( rM / RE, rhoM, 0.05, colM, lw=0.)
ax1.plot( prof.r[:] / RE, prof.rho[:], 'k-', lw=0.3)
ax1.axis([0.2, 1.1, 1.9, 13.5])
ax1.set_title(r'$\mathrm{miscible}$')

(rS, rhoS, pS, colS) = getPoints(dumpS)
ax2 = plt.subplot(221)
ax2.scatter( rS / RE, rhoS, 0.05, colS, lw=0.)
ax2.plot( prof.r[:] / RE, prof.rho[:], 'k-', lw=0.3)
ax2.axis([0.2, 1.1, 1.9, 13.5])
ax2.set_ylabel(r'$\rho [g/cm^3]$')
ax2.set_title(r'$\mathrm{standard}$')

ax3 = plt.subplot(224)
ax3.scatter( rM / RE, pM / 1.e10, 0.05, colM, lw=0.)
ax3.plot( prof.r[:] / RE, prof.p[:] / 1.e10, 'k-', lw=0.3)
ax3.axis([0.2, 1.1, -10., 320.])
ax3.set_xlabel(r'$r [R_E]$')

ax4 = plt.subplot(223)
ax4.scatter( rS / RE, pS / 1.e10, 0.05, colS, lw=0.)
ax4.plot( prof.r[:] / RE, prof.p[:] / 1.e10, 'k-', lw=0.3)
ax4.axis([0.2, 1.1, -10., 320.])
ax4.set_ylabel(r'$p[GPa]$')
ax4.set_xlabel(r'$r[R_E]$')

axs = [ax1, ax2, ax3, ax4]
for ax in axs:
  ax.xaxis.set_major_formatter(tex_formatter)
  ax.yaxis.set_major_formatter(int_formatter)

plt.savefig("out.png")


