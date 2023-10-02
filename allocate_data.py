import os
import shutil
import random

# Set the source dataset directory
dataset_directory = 'datasets'

# Define the destination directories for training, validation, and test sets
train_dir = 'datasets/train_set'
val_dir = 'datasets/val_set'
test_dir = 'datasets/test_set'

# Define the split ratios (70/20/10)
train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1

# Create destination directories if they don't exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Get a list of all files in the dataset directory
all_files = os.listdir(dataset_directory)

# Shuffle the list of files randomly
random.shuffle(all_files)

# Calculate the split indices
total_files = len(all_files)
train_split = int(total_files * train_ratio)
val_split = int(total_files * val_ratio)

# Split the files into training, validation, and test sets
train_files = all_files[:train_split]
val_files = all_files[train_split:train_split + val_split]
test_files = all_files[train_split + val_split:]

# Define a function to check if a file exists in any of the destination directories
def is_file_in_destination(filename):
    return (
        os.path.exists(os.path.join(train_dir, filename))
        or os.path.exists(os.path.join(val_dir, filename))
        or os.path.exists(os.path.join(test_dir, filename))
    )

# Copy files to the respective directories only if they are not already there
for filename in train_files:
    if not is_file_in_destination(filename):
        src = os.path.join(dataset_directory, filename)
        dst = os.path.join(train_dir, filename)
        shutil.copy(src, dst)

for filename in val_files:
    if not is_file_in_destination(filename):
        src = os.path.join(dataset_directory, filename)
        dst = os.path.join(val_dir, filename)
        shutil.copy(src, dst)

for filename in test_files:
    if not is_file_in_destination(filename):
        src = os.path.join(dataset_directory, filename)
        dst = os.path.join(test_dir, filename)
        shutil.copy(src, dst)

print("Dataset split completed.")