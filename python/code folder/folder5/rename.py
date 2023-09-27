import os

# Replace 'your_folder_path' with the path to your folder containing the images.
folder_path = 'C:\\Users\\19079\\Pictures\\code folder'

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Set a counter to start renaming from 1
counter = 1

# Iterate through the files and rename them sequentially
for file_name in files:
    # Check if the file is an image (you can customize this condition)
    if file_name.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
        # Construct the new file name
        new_name = f"josh_{counter:02d}.{file_name.split('.')[-1]}"  # 4-digit zero-padded number
        
        # Construct the full paths for the old and new file names
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        
        # Increment the counter
        counter += 1

print("Renaming complete.")
