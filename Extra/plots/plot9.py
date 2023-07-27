#!/bin/python3
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from plotnine import *

if (len(sys.argv)-1 != 1):
    print("Esqueceste-te do ficheiro (x")
    exit()

df = pd.read_csv(sys.argv[1])

df["BW"]=df["BW"].values.astype(str)

# Fantástico era isto que estivemos à procura durante umas 7 horas
df = df.pivot_table('bit_errors','BW', 'N')

df.reset_index( drop=False, inplace=True )
df.reindex(['BW'], axis=1)
print(df)

# ---- from gallery ----

# Initialize the figure style
plt.style.use('seaborn-v0_8-pastel')
 
# create a color palette
palette = plt.get_cmap('tab10')
 
# multiple line plot
num=0
for column in df.drop('BW', axis=1):
    num+=1
 
    # Find the right spot on the plot
    ax=plt.subplot(3, 3, num)

    for v in df.drop('BW', axis=1):
        plt.plot(df['BW'], df[v], marker='', color='grey', linewidth=0.6, linestyle='dashed', alpha=0.3)
 
    # Plot the lineplot
    plt.plot(df['BW'], df[column], marker='', color=palette(num), linewidth=1.4, alpha=0.9, label=column)
 
    # Same limits for every chart
    plt.xlim(0,41)
    plt.ylim(0,150)
    plt.xticks([df['BW'].min(), df['BW'].max()])
 
    # Add title
    ax.text(.5,.9,'Noise voltage = ' + str(column),
            fontsize=10, fontweight=0, color=palette(num),
            horizontalalignment='center',
            transform=ax.transAxes)
    plt.xlabel('Loop bandwidth', labelpad=-10)
    plt.ylabel('Number of bit errors')
 
# Show the graph
plt.show()
