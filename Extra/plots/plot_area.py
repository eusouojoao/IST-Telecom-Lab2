#!/usr/bin/python3
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from plotnine import *

if (len(sys.argv)-1 != 1):
    print("Esqueceste-te do ficheiro (x")
    exit()

df = pd.read_csv(sys.argv[1])

BW = df["BW"].to_numpy()
N1 = df["N1"].to_numpy()
N4 = df["N4"].to_numpy()

print(N1)

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Plot lines
ax.plot(BW, N4, color="green", label="TED Kp = 4.3415")
ax.plot(BW, N1, color="red", label="TED Kp = 1.0")
ax.legend(loc='upper left', frameon=False)

# Fill area when income > expenses with green
a1 = ax.fill_between(
    BW, N1, N4, where=(N1 > N4), 
    interpolate=True, color="green", alpha=0.25, 
    label="Positive"
)

# Fill area when income <= expenses with red
a2 = ax.fill_between(
    BW, N1, N4, where=(N1 <= N4), 
    interpolate=True, color="red", alpha=0.25,
    label="Negative"
)

plt.title("Noise voltage = 1.0 V")
plt.xlabel('Loop Bandwidth', labelpad=-10)
plt.ylabel('Number of Bit Errors')

from matplotlib.legend import Legend
leg = Legend(ax, [a1, a2], ['Positive', 'Negative'], loc='upper right')
ax.add_artist(leg)
plt.show();
