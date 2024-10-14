import os
from collections import defaultdict

# Set your folder path here
#folder_path = "/home/hbhcm/9"
folder_path = input("Enter Folder : ")

# Dictionary to store images with the same name
image_dict = defaultdict(list)

# Walk through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
        # Get the base name without extension
        name = os.path.splitext(filename)[0]
        image_dict[name].append(filename)

# Delete images that don't have duplicates (i.e., not sharing the same name)
for name, files in image_dict.items():
    if len(files) == 1:
        file_to_delete = os.path.join(folder_path, files[0])
        print(f"Deleting: {file_to_delete}")
        os.remove(file_to_delete)

print("Deletion process completed.")
