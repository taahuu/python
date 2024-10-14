import os
import shutil

def copy_jpg_files(source_folder, destination_folder):
    # Check if destination folder exists, if not, create it
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Loop through all files in the source folder
    for filename in os.listdir(source_folder):
        # Check if the file has a .jpg extension
        if filename.endswith('.jpg'):
            # Construct full file path
            source_file = os.path.join(source_folder, filename)
            destination_file = os.path.join(destination_folder, filename)
            
            # Copy the file
            shutil.copy(source_file, destination_file)
            print(f"Copied: {filename}")

# Example usage
source_folder = '/home/hbhcm/HBH_data_ppr/train/1 (copy)'
destination_folder = '/home/hbhcm/HBH_data_ppr/train/error'

copy_jpg_files(source_folder, destination_folder)
