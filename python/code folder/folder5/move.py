import os
import shutil

# Replace 'your_source_folder' with the path to the folder containing the 50 images.
source_folder = 'C:\\Users\\19079\\Pictures\\code folder'

# Create five destination folders if they don't exist already.
destination_folders = ['folder1', 'folder2', 'folder3', 'folder4', 'folder5']
for folder in destination_folders:
    os.makedirs(folder, exist_ok=True)

# Get a list of all files in the source folder
files = os.listdir(source_folder)

# Calculate how many files should be moved to each destination folder
files_per_folder = len(files) // len(destination_folders)
remainder = len(files) % len(destination_folders)

# Initialize a counter to keep track of files moved
counter = 0

# Iterate through the destination folders
for folder in destination_folders:
    # Determine how many files to move to this folder
    num_files_to_move = files_per_folder + (1 if remainder > 0 else 0)
    remainder -= 1

    # Move the files to the destination folder
    for i in range(num_files_to_move):
        if counter >= len(files):
            break
        file_to_move = files[counter]
        source_path = os.path.join(source_folder, file_to_move)
        destination_path = os.path.join(folder, file_to_move)
        
        # Check if the file is not a folder and if the source and destination are different
        if not os.path.isdir(source_path) and source_path != destination_path:
            shutil.move(source_path, destination_path)
            
        counter += 1

print("Distribution of images into folders complete.")
