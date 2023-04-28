 
import os

# Define the folders and files to be created
folders = ['data', 'themes', 'streamlit']
files = ['streamlit/app.py', 'streamlit/config.toml']

# Create the folders
for folder in folders:
    os.makedirs(folder)

# Create the files
for file in files:
    with open(file, 'w') as f:
        pass
