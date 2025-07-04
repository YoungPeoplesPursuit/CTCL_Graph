import pandas as pd
from lifelines import AalenJohansenFitter
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


#Increase font size, line width, key size, grid number size
#Matplotlib controls for everything

#Order: MF, SS, PALCL, SPTCL

# Change default linewidth
mpl.rcParams['lines.linewidth'] = 2

# Change default figure size
fig, axes = plt.subplots(2, 2, figsize=(8, 6))  # 2x2 grid of plots

plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, hspace=0.2, wspace=0.2)

# Change default font size
mpl.rcParams['font.size'] = 14

###################################################SS#############################################################
SS = pd.read_csv('SS_CM.csv')
aj = AalenJohansenFitter()

#SS['time'] = SS['time'] + np.random.uniform(0, 0.01, size=len(SS)) these r way too laggy

aj.fit(durations=SS['time'], event_observed=SS['status'], event_of_interest=1, label='NHL/CTCL')
plt.subplot(2,2,2)
ax = aj.plot_cumulative_density(ci_show=False, linestyle='-', color='black')

aj.fit(durations=SS['time'], event_observed=SS['status'], event_of_interest=2, label='Infection')
aj.plot_cumulative_density(ax=ax, ci_show=False, linestyle=':', color='blue')  # Use the same axes to overlay onto the same plot

#When customizing get rid of the confidence intervals, change line color and dot style for each line

aj.fit(durations=SS['time'], event_observed=SS['status'], event_of_interest=3, label='Other')
aj.plot_cumulative_density(ax=ax, ci_show=False, linestyle='-', color='red')

aj.fit(durations=SS['time'], event_observed=SS['status'], event_of_interest=4, label='Cardiovascular')
aj.plot_cumulative_density(ax=ax, ci_show=False, linestyle=':', color='black')

aj.fit(durations=SS['time'], event_observed=SS['status'], event_of_interest=5, label='Secondary Primary Cancer')
aj.plot_cumulative_density(ax=ax, ci_show=False, linestyle='-', color='blue')

aj.fit(durations=SS['time'], event_observed=SS['status'], event_of_interest=6, label='Unknown')
aj.plot_cumulative_density(ax=ax, ci_show=False, linestyle=':', color='red')

plt.title("SS")
plt.xlabel("")
plt.ylabel("Cumulative Incidence")






#####################################################MF##############################################################
MF = pd.read_csv('MF_CM.csv')
aj = AalenJohansenFitter()

#MF['time'] = MF['time'] + np.random.uniform(0, 0.01, size=len(MF))

aj.fit(durations=MF['time'], event_observed=MF['status'], event_of_interest=1, label='NHL/CTCL')
plt.subplot(2,2,1)
ax = aj.plot_cumulative_density(ci_show=False, linestyle='-', color='black')

aj.fit(durations=MF['time'], event_observed=MF['status'], event_of_interest=2, label='Infection')
aj.plot_cumulative_density(ax=ax, ci_show=False, linestyle=':', color='blue')  # Use the same axes to overlay onto the same plot

#When customizing get rid of the confidence intervals, change line color and dot style for each line

aj.fit(durations=MF['time'], event_observed=MF['status'], event_of_interest=3, label='Other')
aj.plot_cumulative_density(ax=ax, ci_show=False, linestyle='-', color='red')

aj.fit(durations=MF['time'], event_observed=MF['status'], event_of_interest=4, label='Cardiovascular')
aj.plot_cumulative_density(ax=ax, ci_show=False, linestyle=':', color='black')

aj.fit(durations=MF['time'], event_observed=MF['status'], event_of_interest=5, label='Secondary Primary Cancer')
aj.plot_cumulative_density(ax=ax, ci_show=False, linestyle='-', color='blue')

aj.fit(durations=MF['time'], event_observed=MF['status'], event_of_interest=6, label='Unknown')
aj.plot_cumulative_density(ax=ax, ci_show=False, linestyle=':', color='red')

plt.title("MF")
plt.xlabel("")
plt.ylabel("Cumulative Incidence")


#####################################################PALCL##############################################################
ALCL = pd.read_csv('ALCL_CM.csv')
aj = AalenJohansenFitter()

# Get rid of that space
ALCL.columns = ALCL.columns.str.strip()

# Optional: Handle ties explicitly by jittering the 'time' column
#ALCL['time'] = ALCL['time'] + np.random.uniform(0, 0.01, size=len(ALCL))

aj.fit(durations=ALCL['time'], event_observed=ALCL['status'], event_of_interest=1, label='NHL/CTCL')
plt.subplot(2,2,3)
ax = aj.plot_cumulative_density(ci_show=False, linestyle='-', color='black')

aj.fit(durations=ALCL['time'], event_observed=ALCL['status'], event_of_interest=2, label='Infection')
aj.plot_cumulative_density(ax=ax, ci_show=False, linestyle=':', color='blue')  # Use the same axes to overlay onto the same plot

#When customizing get rid of the confidence intervals, change line color and dot style for each line

aj.fit(durations=ALCL['time'], event_observed=ALCL['status'], event_of_interest=3, label='Other')
aj.plot_cumulative_density(ax=ax, ci_show=False, linestyle='-', color='red')

aj.fit(durations=ALCL['time'], event_observed=ALCL['status'], event_of_interest=4, label='Cardiovascular')
aj.plot_cumulative_density(ax=ax, ci_show=False, linestyle=':', color='black')

aj.fit(durations=ALCL['time'], event_observed=ALCL['status'], event_of_interest=5, label='Secondary Primary Cancer')
aj.plot_cumulative_density(ax=ax, ci_show=False, linestyle='-', color='blue')

aj.fit(durations=ALCL['time'], event_observed=ALCL['status'], event_of_interest=6, label='Unknown')
aj.plot_cumulative_density(ax=ax, ci_show=False, linestyle=':', color='red')

plt.title("ALCL")
plt.xlabel("Months")
plt.ylabel("Cumulative Incidence")


#####################################################SPTCL##############################################################
SPTCL = pd.read_csv('SPTCL_CM.csv')
aj = AalenJohansenFitter()

#SPTCL['time'] = SPTCL['time'] + np.random.uniform(0, 0.01, size=len(SPTCL))

aj.fit(durations=SPTCL['time'], event_observed=SPTCL['status'], event_of_interest=1, label='NHL/CTCL')
plt.subplot(2,2,4)
ax = aj.plot_cumulative_density(ci_show=False, linestyle='-', color='black')

aj.fit(durations=SPTCL['time'], event_observed=SPTCL['status'], event_of_interest=2, label='Infection')
aj.plot_cumulative_density(ax=ax, ci_show=False, linestyle=':', color='blue')  # Use the same axes to overlay onto the same plot

#When customizing get rid of the confidence intervals, change line color and dot style for each line

aj.fit(durations=SPTCL['time'], event_observed=SPTCL['status'], event_of_interest=3, label='Other')
aj.plot_cumulative_density(ax=ax, ci_show=False, linestyle='-', color='red')

aj.fit(durations=SPTCL['time'], event_observed=SPTCL['status'], event_of_interest=4, label='Cardiovascular')
aj.plot_cumulative_density(ax=ax, ci_show=False, linestyle=':', color='black')

aj.fit(durations=SPTCL['time'], event_observed=SPTCL['status'], event_of_interest=5, label='Secondary Primary Cancer')
aj.plot_cumulative_density(ax=ax, ci_show=False, linestyle='-', color='blue')

aj.fit(durations=SPTCL['time'], event_observed=SPTCL['status'], event_of_interest=6, label='Unknown')
aj.plot_cumulative_density(ax=ax, ci_show=False, linestyle=':', color='red')

plt.title("SPTCL")
plt.xlabel("Months")
plt.ylabel("CTCL_CIF")


for ax in fig.axes:  # Loop through all subplots
    ax.set_ylim(0, 0.6)  # Set the y-axis range from 0 to 0.6
    ax.legend(loc="upper left", prop={'size': 6}) # Move those legends

plt.savefig("CTCL_CIF.png", dpi=300, bbox_inches="tight")
plt.show()



