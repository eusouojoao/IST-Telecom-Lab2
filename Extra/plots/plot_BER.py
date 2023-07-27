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
print(df)
N0 = df["N0"].to_numpy()
BPSK = df["BPSK"].to_numpy()
QPSK = df["QPSK"].to_numpy()
TEO = df["TEO"].to_numpy()

# Initialize the figure style
plt.style.use('seaborn-v0_8-pastel')

# Plots
plt.plot(N0, BPSK, marker='o', color='red', linewidth=1.2, alpha=0.9, label="BPSK")
plt.plot(N0, QPSK, marker='o', color='green', linewidth=1.2, alpha=0.9, label="QPSK")
plt.plot(N0, TEO, marker='o', color='black', linestyle='dashed', linewidth=1.5, alpha=0.9, label="Curva teórica")

# Scales
plt.xscale('linear')
plt.yscale('log')
plt.grid(True,'both',linestyle='--')

plt.xlim(0.5,4)

# Add title
plt.xlabel('Noise voltage [V]',size=16)
plt.ylabel('Bit Error Rate (BER)',size=16)
plt.title('Probabilidade de erro de bit em escala semi-log',size=32)
plt.rc('legend', fontsize=14)
plt.legend(loc='best', fancybox=True, framealpha=1)

# Show the graph
plt.show()
