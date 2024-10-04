import os
import shutil
import platform
import subprocess

# Define the source directory (Downloads folder)
source_dir = os.path.expanduser("~/Documents")

# Define target folders for different file types
folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv"],
    "Installers": [".exe", ".dmg", ".msi", ".zip", ".tar", ".gz"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Video": [".mp4", ".mkv", ".mov", ".avi"],
    "Others": []  # Any other file types will go here
}

# Create target directories if they don't exist
for folder in folders.keys():
    os.makedirs(os.path.join(source_dir, folder), exist_ok=True)

# Move files into appropriate folders
for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Get the file extension
    _, file_extension = os.path.splitext(filename)
    file_extension = file_extension.lower()

    # Find the appropriate folder for the file
    moved = False
    for folder, extensions in folders.items():
        if file_extension in extensions:
            shutil.move(file_path, os.path.join(source_dir, folder, filename))
            moved = True
            break

    # If the file type doesn't match any of the predefined types, move to "Others"
    if not moved:
        shutil.move(file_path, os.path.join(source_dir, "Others", filename))

print("File organization complete.")

# Open the Downloads folder
system_platform = platform.system()

try:
    if system_platform == "Windows":
        os.startfile(source_dir)
    elif system_platform == "Darwin":  # macOS
        subprocess.run(["open", source_dir])
    elif system_platform == "Linux":
        subprocess.run(["xdg-open", source_dir])
    else:
        print("Unsupported Operating System: Unable to open the Downloads folder automatically.")
except Exception as e:
    print(f"An error occurred while trying to open the Downloads folder: {e}")
