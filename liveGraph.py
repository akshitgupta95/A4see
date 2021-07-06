
import pandas as pd
import numpy as np
import math
import datetime
import scipy
import glob
# import pingouin as pg
# import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency 
import matplotlib.animation as animation
# import statsmodels.api as sm
# import statsmodels.formula.api as smf

# Set the default Pandas float precision to 3 decimals
pd.set_option("display.precision", 3)
# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
y1s = []
y2s = []
y3s = []
y4s = []



# This function is called periodically from FuncAnimation
def animate(i,xs,y1s,y2s,y3s,y4s):
    for f in glob.glob('*measurement*.envisible'):
        data = pd.read_csv(f,sep='\t',skiprows=15)
        data = data.iloc[1:]
        data["CH0"]=data.CH0.astype(float)
        data["CH1"]=data.CH1.astype(float)
        data["CH2"]=data.CH2.astype(float)
        data["CH3"]=data.CH3.astype(float)
        data["ElapsedTime"]=data.ElapsedTime.astype(float)

        # Add x and y to lists
        
        print('CH1',data["CH0"].tail(1))
        print('CH2',data["CH1"].tail(1))
        print('CH3',data["CH2"].tail(1))
        print('CH4',data["CH3"].tail(1))
        xs.append(data["ElapsedTime"].tail(1))
        y1s.append(data["CH0"].tail(1))
        y2s.append(data["CH1"].tail(1))
        y3s.append(data["CH2"].tail(1))
        y4s.append(data["CH3"].tail(1))

        # Limit x and y lists to 20 items
        xs = xs[-20:]
        y1s = y1s[-20:]
        y2s = y2s[-20:]
        y3s = y3s[-20:]
        y4s = y4s[-20:]

        # Draw x and y lists
        ax.clear()
        ax.plot(xs, y1s, label='channel-1')
        ax.plot(xs, y2s, label='channel-2')
        ax.plot(xs, y3s, label='channel-3')
        ax.plot(xs, y4s, label='channel-4')

        # Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('Readings over time over Time')
        plt.ylabel('Voltage Values')
        plt.legend()

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs,y1s,y2s,y3s,y4s), interval=1000)

plt.show()