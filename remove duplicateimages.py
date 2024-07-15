import os
import hashlib
import shutil

def remove_duplicate_images(folder_path):
  """Removes duplicate images from the specified folder.

  Args:
    folder_path: The path to the folder containing the images.
  """

  file_hashes = {}
  duplicate_files = []

  for root, _, files in os.walk(folder_path):
    for file in files:
      file_path = os.path.join(root, file)
      if file_path.lower().endswith(('.jpg', '.jpeg', '.png')):
        with open(file_path, 'rb') as f:
          file_hash = hashlib.md5(f.read()).hexdigest()

        if file_hash in file_hashes:
          duplicate_files.append(file_path)
        else:
          file_hashes[file_hash] = file_path

  # Remove duplicate files
  for file_path in duplicate_files:
    try:
      os.remove(file_path)
      print(f"Removed duplicate file: {file_path}")
    except OSError as e:
      print(f"Error removing file: {file_path}, {e}")

if __name__ == '__main__':
  folder_path = input("Enter the folder path: ")
  remove_duplicate_images(folder_path)
