# Gait Phase Classifier for Roam Knee Exoskeleton
***
Developed a classification machine learning model to determine gait phase based on unique [Roam exoskeleton](https://www.roamrobotics.com/) sensor output.  

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
  
## Project Motivation

## Data Processing
## Model Training
## Hyperparameter Tuning
## Model Performance Visualization
## Bonus: Stick Figure Simulation
