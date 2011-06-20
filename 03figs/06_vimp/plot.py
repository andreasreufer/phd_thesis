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


plt.figure( figsize=(5,4) )

ax1 = plt.subplot(111)
#ax1.set_xlabel(r'$\theta_{imp}$')
#ax1.set_ylabel(r'$V_{hit,imp} / V_{imp}$')

ax1.set_xlabel(r'$R [AU]$')
ax1.set_ylabel(r'$e$')

#vk = sqrt( G*M / R )
#vimp = e*vk

#-> e = vimp / vk = vimp*sqrt( R / G*M)


csound = 3.68e5 # 3.68km/s
vimpA = 1.e6    # 10km/s
vimpB = 1.e5    #  1km/s
vimpC = 1.e4    # .1km/s

R = np.logspace( -2., 2. )

#ax1.loglog( 
ax1.loglog( R, vimpA*np.sqrt( AU*R / (G*MS) ), 'k--' )
ax1.loglog( R, vimpB*np.sqrt( AU*R / (G*MS) ), 'k--' )
ax1.loglog( R, vimpC*np.sqrt( AU*R / (G*MS) ), 'k--' )
ax1.loglog( R, csound*np.sqrt( AU*R / (G*MS) ), 'r' )

ax1.text( 0.1, 0.4, "$v_{rand} = 10 km/s$", rotation=26.)
ax1.text( 0.1, 0.04, "$v_{rand} =  1 km/s$", rotation=26.)
ax1.text( 0.1, 0.0040, "$v_{rand} = 0.1km/s$", rotation=26.)
ax1.text( 0.1, 0.0040, "$v_{rand} = 0.1km/s$", rotation=26.)

ax1.text( 0.1, 0.17, "$c_{SiO_{2}} = 3.68 km/s$", rotation=26.)

ax1.text( 0.02, 0.6, r"$v_{rand} \approx e v_{Kepler}$" )

#ax1.text( 0.1, 0.4, "$v_{rand} = 10 km/s$", rotation=28.)
#ax1.text( 0.1, 0.1, "$10 km/s$", rotation=28.)
#ax1.text( 0.1, 0.1, "$10 km/s$", rotation=28.)

#ax1.text( 0.1, 0.1, "$10 km/s$", rotation=28.)

ax1.axis([0.015, 50., 1.e-3, 1.0])

ax1.xaxis.set_major_formatter(math_formatter)
#ax1.yaxis.set_major_formatter(math_formatter)


bgax = plt.axes( [0., 0., 1., 1.], frameon=False)
#bgax.text( 0.4, 0.9, "haba", size=20)
bgax.axis([0., 1., 0., 1.])
bgax.xaxis.set_ticks( [] )
bgax.yaxis.set_ticks( [] )


plt.savefig("out.pdf")



