import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import argparse


parser=argparse.ArgumentParser(description="Plot Nonin DATA from CSV file")
parser.add_argument("file_name",help="File Name", type=str)
args=parser.parse_args()


plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()

max_len = 5*75

def animate(i):
    data = pd.read_csv(args.file_name)
    x = data['time'].tail(max_len)
    y1 = data['waveform'].tail(max_len)
  

    plt.cla()

    plt.plot(x, y1, label='Channel 1')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=300)

plt.tight_layout()
plt.show()