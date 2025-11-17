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

### 3. Stick Figure Simulation
Code will generate a visualization of timed actuation assistance of a stick figure on a treadmill.  
- Input: inverse kinematic .mot file
- Output: demo walking figure .gif file  

***
  
## Installations and Setup
### 1. Ground Truth Event Labeling
- Download fp_synced.csv and exo_synced.csv (from [Google Drive](https://drive.google.com/drive/folders/114_iw5vM-oKkxQ3ksYX6KxAR6FYzifeX?usp=sharing))  
* `pip install scipy`  

### 2. Hyperparameter Tuning and Classification ML
- Download alldata_[a-e].csv (from [Google Drive](https://drive.google.com/drive/folders/114_iw5vM-oKkxQ3ksYX6KxAR6FYzifeX?usp=sharing))  
* `pip install optuna`  
- For CPU only: 
`pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu`  
* For GPU with CUDA: 
`pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118`  

### 3. Stick Figure Simulation  
- Download InverseKinematics_GaitData.mot
  
*** 

## Project Motivation

## Data Processing
## Model Training
## Hyperparameter Tuning
## Model Performance Visualization
## Bonus: Stick Figure Simulation
