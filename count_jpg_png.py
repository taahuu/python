import os

def count_image_files(directory):
    # Initialize counters
    jpg_count = 0
    png_count = 0
    
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a .jpg or .png
        if filename.lower().endswith('.jpg'):
            jpg_count += 1
        elif filename.lower().endswith('.png'):
            png_count += 1

    # Print the result
    print(f"Number of .jpg files: {jpg_count}")
    print(f"Number of .png files: {png_count}")

# Specify the directory
directory_path = '/home/hbhcm/HBH_data_ppr/Arc Flash TAHA'

# Call the function
count_image_files(directory_path)
