# Gait Phase Classifier for Roam Knee Exoskeleton

Develop a classification machine learning model to determine gait phase based on unique [Roam exoskeleton](https://www.roamrobotics.com/) sensor output.  
***

## Outline  
### 1. Ground Truth Event Labeling  
Example code will demonstrate the process of: taking in 2 synced data files, filtering force plate data, finding the heel-strike and toe-offs through threshold windowing, and labeling these ground truth labels in the exoskeleton sensor data file.  
- Input: force plate and exoskeleton synced .csv files
- Output: labeled exoskeleton data

### 2. Hyperparameter Tuning and Classification ML
Binarized code will perform hyperparameter tuning using Optuna and will train a classification ML model to detect key gait phases.  
- Input: labeled exoskeleton .csv files  
- Output: optimal hyperparameter values and model accuracy  

### 3. Bonus Stick Figure Simulation
Code will generate a visualization of timed actuation assistance of a stick figure on a treadmill.  
- Input: inverse kinematic .mot file
- Output: demo walking figure .gif file  

***
  
## Installations and Setup
### 1. Ground Truth Event Labeling
- Download fp_synced.csv and exo_synced.csv (from [UT Box]([https://utexas.box.com/s/lyaur3cgd2ui4627rupvltib57bmxn82]))  
- `pip install scipy`  

### 2. Hyperparameter Tuning and Classification ML
- Download alldata_[a-e]_trim.csv (from [UT Box](https://utexas.box.com/s/lyaur3cgd2ui4627rupvltib57bmxn82))
- Download TCN_Training binary executables (from [UT Box](https://utexas.box.com/s/lyaur3cgd2ui4627rupvltib57bmxn82))
  - TCN_Training_binary_3_epoch.exe trains for 3 epochs (Much shorter)
  - TCN_Training_binary.exe trains for 50 epochs

#### a) For Windows  
- Run TCN_Training_binary_3_epoch_Windows.exe *might take a few minutes to run*
- Select project folder
- Select training data
- Select testing data
- Output: training_results folder

#### b) For Mac
- Run TCN_Training_binary_3_epoch_mac.exe *might take a few minutes to run*
- Select project folder
- Select training data
- Select testing data
- Do NOT select any more directories if prompted
- Output: training_results folder

### 3. Bonus Stick Figure Simulation  
- Download InverseKinematics_GaitData.mot
  
