# GeoGuesser AI Bot


## Project Overview

This project is an AI-powered bot inspired by the popular web game GeoGuessr. The goal is to identify the country from a single street view image. We leverage OpenAI's powerful CLIP (Contrastive Language-Image Pre-training) model, fine-tuning it on a dataset of over 50,000 geolocation images to specialize it for this task.

The final application, `bot.py`, runs in the background, listening for a key press. When activated, it takes a screenshot of the user's screen, processes it, and feeds it into our fine-tuned model to predict the country, displaying the top 5 most likely locations with their confidence scores.

---

## Setup Guide

Follow these steps to set up the project on your local machine.

### 1. Prerequisites
- Python 3.8+
- `pip` and `venv`

### 2. Virtual Environment
It is highly recommended to create a virtual environment to manage project dependencies.

```bash
# Create a virtual environment named 'venv'
python -m venv venv

# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```
For more details, see the official guide on creating virtual environments.

### 3. Install Dependencies
With your virtual environment activated, install the required packages.
For users with an NVIDIA GPU and CUDA installed:

```bash
python -m pip install -r requirements-cuda.txt
```

For users without a dedicated NVIDIA GPU (CPU-only):

```bash 
python -m pip install -r requirements.txt
```

### 4. Dataset

The full, pre-processed dataset is 7GB and is available on Kaggle.
Download the dataset from this Kaggle link:
https://www.kaggle.com/datasets/ubitquitin/geolocation-geoguessr-images-50k

You will get an archive.zip file.
Inside your local project directory (the one containing this README), create a folder named compressed_dataset.
Unzip the contents of archive.zip directly into the compressed_dataset folder.
The final folder structure should look like this:

```
your-project-root/
├── compressed_dataset/
│   ├── Argentina/
│   ├── Australia/
│   ├── ... (other country folders)
├── models/
├── augment.py
├── bot.py
└── ... (other project files)
```

### 5. Pre-trained Models
Our fine-tuned model weights are available in the project's Google Drive.
#### 1. Create a folder named models in the root of your project directory.
#### 2. Download the .pt model file from the Google Drive and place it inside this models folder.

## Usage
### Running the GeoBot
#### 1. The main application is the real-time prediction bot.
#### 2. Make sure you have a street view image visible on your screen (e.g., from Google Maps, GeoGuessr, etc.).
#### 3. Run the bot script from your terminal:
```bash
python bot.py
```
#### 4. You will see a message "model is ready!". The script is now listening for your input.
#### 5. Press the n key to take a screenshot and get a prediction. The top 5 results will be printed to your terminal.

### Project Scripts Overview
combine_data.ipynb: The initial script used to source data from the Hugging Face marcelomoreno26/geoguessr dataset and organize it into the required folder structure.

augment.py: A script to perform data augmentation (flipping, cropping) on classes with fewer than 100 images to help balance the dataset.

final_project.ipynb: The main Jupyter Notebook containing the entire model fine-tuning process. This is where we defined our custom dataset, set up the training loop, and trained the CLIP model.

bot.py: The final application for real-time inference. It uses pyautogui for screenshots and pynput for keyboard listening.
