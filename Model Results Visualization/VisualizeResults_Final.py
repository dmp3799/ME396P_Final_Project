#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 11:42:50 2025

@author: helenemerson
"""

# Import packages: use scipy.signal for filtering and matplotlib for visualization
import numpy as np
import pandas as pd
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt

# 1. IMPORT EXPERIMENTAL DATA AND GROUND TRUTH LABELS
# -----------------------------------------------------------------------------
data = pd.read_csv('alldata_a_trim.csv')

# Pull columns that I will filter and plot
find_knee_angles = filter(lambda item: 'knee_angle' in item[0], data.items())
knee_angles = dict(find_knee_angles)

# Store labels
find_labels = filter(lambda item: ('events' in item[0]) or ('Phase' in item[0]), data.items())
labels = dict(find_labels)

# Store time
store_time = np.asarray(data['Time'])
# Time is in DT notation - change to plain seconds for ease of plotting
time = np.linspace(0, len(store_time)/175, len(store_time))

# Convert to numpy array and degrees
for key, values in knee_angles.items():
    knee_angles[key] = np.asarray(values, dtype=float) * 180/np.pi

# Define functions for filtering
def lowpass(cutoff_hz, fs, order=4):
    nyq = 0.5 * fs
    b, a = butter(order, cutoff_hz/nyq, btype='low', analog=False)
    return b, a
def apply_filtfilt(sig, cutoff_hz, fs, order=4):
    b, a = lowpass(cutoff_hz, fs, order=order)
    return filtfilt(b, a, sig, method='pad')

# Set up filter parameters
cutoff = 6.0
fs = 150 

# Filter knee angles 
filtered_knee_angles = {}
for key, values in knee_angles.items():
    filtered_knee_angles[key] = apply_filtfilt(values, cutoff, fs)

# 2. IMPORT MODEL PREDICTION DATA
# -----------------------------------------------------------------------------

# Trim predictions, experimental so that it aligns with the last 10%-150 frames
# of the experimental trial (first quarter of prediction)
# predictions = pd.read_csv('predictions.csv')
predictions = pd.read_csv('evaluation_trial_a_4.csv')

viz_offset = 610
experimental_portion = int(np.round(0.9*(len(time)-1000)+150))+viz_offset
#experimental_portion = int(np.round(0.1*len(time)+150))

# pred_length = int(len(time)-(experimental_portion))

plot_time = time[experimental_portion:-1200]
pred_length = len(plot_time)
#plot_time = time[experimental_portion:temp_end]
plot_knee_angles_R = filtered_knee_angles['right__knee_knee_angle_159_'][experimental_portion:-1200]
plot_knee_angles_L = filtered_knee_angles['left__knee_knee_angle_117_'][experimental_portion:-1200]

# plot_events_R = labels['R_events'][experimental_portion::]
# plot_events_L = labels['L_events'][experimental_portion::]

# plot_predictions_R = list(map(lambda x: np.round(x), predictions['pred_prob_0'][0:pred_length]))
# plot_predictions_L = list(map(lambda x: np.round(x), predictions['pred_prob_1'][0:pred_length]))

plot_predictions_R = list(map(lambda x: np.round(x), predictions['prob_R'][viz_offset:viz_offset+pred_length]))
plot_predictions_L = list(map(lambda x: np.round(x), predictions['prob_L'][viz_offset:viz_offset+pred_length]))

transitions_R = np.where(np.diff(plot_predictions_R) != 0)[0]
transitions_L = np.where(np.diff(plot_predictions_L) != 0)[0]

bounds_R = np.concatenate(([0], transitions_R+1, [len(plot_predictions_R)]))
bounds_L = np.concatenate(([0], transitions_L+1, [len(plot_predictions_L)]))

plot_gt_R = predictions['true_R'][viz_offset:viz_offset+pred_length]
plot_gt_L = predictions['true_L'][viz_offset:viz_offset+pred_length]

transitions_gt_R = np.where(np.diff(plot_gt_R) != 0)[0]
transitions_gt_L = np.where(np.diff(plot_gt_L) != 0)[0]

bounds_gt_R = np.concatenate(([0], transitions_gt_R+1, [len(plot_gt_R)]))
bounds_gt_L = np.concatenate(([0], transitions_gt_L+1, [len(plot_gt_L)]))
# Remove extra line at beginning 
bounds_gt_L = bounds_gt_L[bounds_gt_L > 0]


# 3. PLOT TO VISUALIZE GROUND TRUTH + MODEL RESULTS
# -----------------------------------------------------------------------------
fig, axs = plt.subplots(2, 1, figsize=(10, 6), sharex=True)    

# Legend controls
show_TO = False
show_HS = False
show_swing = False
show_stance = False

# RIGHT LEG
axs[0].plot(plot_time, plot_knee_angles_R)
for start, end in zip(bounds_R[:-1], bounds_R[1:]):
    phase_value = plot_predictions_R[start]

    # Pick color for swing/stance
    if phase_value == 1:
        color = 'lightblue'   # swing
    else:
        color = 'red'  # stance
    try:
        if color == 'lightblue':
            if not show_swing and end<len(plot_time)-1:
                axs[0].axvspan(plot_time[start], plot_time[end], color=color, alpha=0.25, label = 'Predicted Stance')
                show_swing = True
            else:
                axs[0].axvspan(plot_time[start], plot_time[end], color=color, alpha=0.25)
        if color == 'red' and end<len(plot_time)-1:
            if not show_stance:
                axs[0].axvspan(plot_time[start], plot_time[end], color=color, alpha=0.25, label = 'Predicted Swing')
                show_stance = True
            else:
                axs[0].axvspan(plot_time[start], plot_time[end], color=color, alpha=0.25)
        if end>=len(plot_time):
            axs[0].axvspan(plot_time[start], plot_time[-1], color=color, alpha=0.25)
    except IndexError:
        pass
        # if end>plot_time[::-1]:
        #     axs[0].axvspan(plot_time[start], plot_time[::-1], color=color, alpha=0.25)

            
try:
    for start, end in zip(bounds_gt_R[:-1], bounds_gt_R[1:]):
        axs[0].axvline(plot_time[start], color='black')
        axs[0].axvline(plot_time[end], color='black')
except IndexError:
    pass
axs[0].legend(loc='upper left')
axs[0].set_xlim(plot_time[0], plot_time[-1])
axs[0].set_ylabel('Angle (deg)')
axs[0].set_title('Right Knee')
axs[0].grid(True)

# LEFT LEG
axs[1].plot(plot_time, plot_knee_angles_L)
for start, end in zip(bounds_L[:-1], bounds_L[1:]):
    phase_value = plot_predictions_L[start]

    # Pick color for swing/stance
    if phase_value == 1:
        color = 'lightblue'   # swing
    else:
        color = 'red'  # stance
    try:
        if end<len(plot_time)-1:
            axs[1].axvspan(plot_time[start], plot_time[end], color=color, alpha=0.25)
        elif end>=len(plot_time):
            axs[1].axvspan(plot_time[start], plot_time[-1], color=color, alpha=0.25)
    except IndexError:
        pass
try:
    # Add HS/TO Labels
    # WHY IS THERRE EXTRA LINE AT THE BEGINNING
    for start, end in zip(bounds_gt_L[:-1], bounds_gt_L[1:]):
        axs[1].axvline(plot_time[start], color='black')
        axs[1].axvline(plot_time[end], color='black')
except IndexError:
    pass
axs[1].set_xlim(plot_time[0], plot_time[-1])
axs[1].set_ylabel('Angle (deg)')
axs[1].set_xlabel('Time (s)')
axs[1].set_title('Left Knee')
axs[1].grid(True)

plt.savefig("Group3_ModelResultViz.jpg", dpi=300)
