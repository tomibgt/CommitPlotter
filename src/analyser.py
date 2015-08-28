#!/usr/bin/env python

'''
This script plots the amount of changes done in a given set of GitHub repository,
with the data given in cvs files.
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
import sys
import datetime as dt
import matplotlib
from BgtConfiguration import *

__author__  = "Johannes Holvitie, Tomi 'bgt' Suovuo"
__version__ = "0.1"

def freq(dates, deltas, c, l, h):
    lastDateI = -1
    ax = plt.gca()
    dx = []
    iy = []
    
    for i in range(0,len(dates)):
        if lastDateI == -1:
            lastDateI = i
        else:
            dd = (dates[i] - dates[lastDateI]).days
            if dd <= -7:
                d = dt.datetime.strptime(str(dates[lastDateI]),'%Y-%m-%d').date()
                #i       str(dates[lastDateI])            sum([int(d) for d in deltas[lastDateI:i]])
                dx.append(d)
                iy.append(i)
                ax.add_patch(patches.Rectangle(
                    (d, 0),
                    dd,
                    sum([int(d) for d in deltas[lastDateI:i]]),
                    color=c,
					#fill=None,
                    alpha=0.25))
					#hatch=h))
                lastDateI = -1
    plt.plot_date(dx, iy, fmt=l+c)

def loadAndPlot(path, f, c, l, h):
    data = np.genfromtxt(path, dtype=None, delimiter=";", usecols=[1,5])
    print data
    du = [d.split(" ")[0] for d in data[1:,0]]
    dates = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in du]
    deltas = data[1:,1]
    freq(dates, deltas, c, l, h)
    plt.plot_date(dates, deltas, fmt=f+c, alpha=0.75)

def printHowToUse():
    print "Usage: python analyser.py inputfile.csv"

deprecatedTime = dt.datetime.strptime('5.19.2014','%m.%d.%Y').date()
removedTime = dt.datetime.strptime('4.20.2015','%m.%d.%Y').date()
removedTimeSpaced = dt.datetime.strptime('4.21.2015','%m.%d.%Y').date()
try:
    config = BgtConfiguration()
    config.parseCommandLine(sys.argv)
except BadCommandLineException as e:
    print e.message
    printHowToUse()
    sys.exit()

plt.figure(figsize=(20,9))
loadAndPlot(config.inputfiles[0], 'o', 'r', '-', '/')
#loadAndPlot(root_path + "output.festivals.csv", 'o', 'r', '-.', '/')
#loadAndPlot(root_path + "output.geocaching.csv", 'o', 'g', '-', '')
#loadAndPlot(root_path + "output.sails.csv", '*', 'b', '--', '\\')
#loadAndPlot(root_path + "output.waterlock.csv", 'D', 'g', '-', '|')
plt.yscale('log')
x1,x2,y1,y2 = plt.axis()
plt.axis((dt.datetime.strptime('10.1.2014','%m.%d.%Y').date(),x2,0,100000))
plt.axvline(deprecatedTime, linewidth=2, color='black')
plt.text(deprecatedTime,500,'Deprecation Time',rotation=90, fontsize=20)
plt.axvline(removedTime, linewidth=2, color='black')
plt.text(removedTimeSpaced,6000,'Removal Time\n(May 20, 2015)',rotation=90, fontsize=20)
plt.tight_layout()
ax = plt.gca()
for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] + ax.get_xticklabels() + ax.get_yticklabels()):
	item.set_fontsize(20)
plt.show()