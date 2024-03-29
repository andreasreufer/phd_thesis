#!/usr/bin/env ipython
import numpy as np
import matplotlib as mp
mp.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as col
import matplotlib.mpl    as mpl
import tables as pt
import pylab as pl

from gi_plot import *
from h5part import H5PartDump
from plot_helpers import *
from const_cgs import *
from numpy import log10, power

plt.rc('savefig', dpi=300)
mp.rc('text', usetex=True)
#plt.rc('text', usetex=True)
plt.rc('text.latex', preamble = '\usepackage{amssymb}, \usepackage{wasysym}')


plt.figure( figsize=(8,5) )

gammaA = pl.loadtxt("gamma_1.e-3.txt")
gammaB = pl.loadtxt("gamma_0.100.txt")
gammaD = pl.loadtxt("gamma_0.350.txt")
gammaG = pl.loadtxt("gamma_0.900.txt")

ax1 = plt.subplot(221)
ax1.set_xlabel(r'$\theta_{imp}$')
ax1.set_ylabel(r'$V_{hit,imp} / V_{imp}$')

ax1.plot( gammaA[:,1], gammaA[:,2], 'k--' )
ax1.plot( gammaB[:,1], gammaB[:,2], 'r-' )
ax1.plot( gammaD[:,1], gammaD[:,2], 'g-' )
ax1.plot( gammaG[:,1], gammaG[:,2], 'b-' )
ax1.hlines( 0.5, 0., 90., colors='k', linestyles=':')
ax1.axis([0., 90., -0.05, 1.05])
ax1.xaxis.set_label_position("top")


ax2 = plt.subplot(222)
ax2.set_xlabel(r'$\theta_{imp}$')
ax2.set_ylabel(r'$V_{hit,tar} / V_{tar}$')

ax2.plot( gammaA[:,1], gammaA[:,3], 'k--', label=r"$\gamma = 0.001$")
ax2.plot( gammaB[:,1], gammaB[:,3], 'r-', label=r"$\gamma = 0.10$" )
ax2.plot( gammaD[:,1], gammaD[:,3], 'g-', label=r"$\gamma = 0.35$" )
ax2.plot( gammaG[:,1], gammaG[:,3], 'b-', label=r"$\gamma = 0.90$" )
ax2.yaxis.set_label_position("right")
ax2.xaxis.set_label_position("top")
ax2.legend(frameon=False)
ax2.axis([0., 90., -0.05, 1.05])


ax3 = plt.subplot(223)
ax3.set_xlabel(r'$b$')
ax3.set_ylabel(r'$V_{hit,imp} / V_{imp}$')

ax3.plot( gammaA[:,0], gammaA[:,2], 'k--' )
ax3.plot( gammaB[:,0], gammaB[:,2], 'r-' )
ax3.plot( gammaD[:,0], gammaD[:,2], 'g-' )
ax3.plot( gammaG[:,0], gammaG[:,2], 'b-' )
ax3.axis([0., 1.0, -0.05, 1.05])
ax3.hlines( 0.5, 0., 1., colors='k', linestyles=':')


ax4 = plt.subplot(224)
ax4.set_xlabel(r'$b$')
ax4.set_ylabel(r'$V_{hit,tar} / V_{tar}$')

ax4.plot( gammaA[:,0], gammaA[:,3], 'k--', label=r"$\gamma = 0.001$")
ax4.plot( gammaB[:,0], gammaB[:,3], 'r-', label=r"$\gamma = 0.10$" )
ax4.plot( gammaD[:,0], gammaD[:,3], 'g-', label=r"$\gamma = 0.35$" )
ax4.plot( gammaG[:,0], gammaG[:,3], 'b-', label=r"$\gamma = 0.90$" )
ax4.yaxis.set_label_position("right")
ax4.axis([0., 1.0, -0.05, 1.05])

bgax = plt.axes( [0., 0., 1., 1.], frameon=False)
#bgax.text( 0.4, 0.9, "haba", size=20)
bgax.axis([0., 1., 0., 1.])
bgax.xaxis.set_ticks( [] )
bgax.yaxis.set_ticks( [] )


plt.savefig("out.pdf")



