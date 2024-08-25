import os
import shutil

# Set the directory path
directory = r'E:\New folder'

# Create a dictionary to map file extensions to folders
extension_folders = {
    'txt': 'Text Files',
    'docx': 'Word Documents',
    'pdf': 'PDF Files',
    'jpg': 'Image Files',
    'mp3': 'Audio Files',
    'png': 'Image Files'
}

# Iterate through all files in the directory
for filename in os.listdir(directory):
    # Get the file extension
    file_extension = os.path.splitext(filename)[1][1:]

    # Check if the file extension is in the dictionary
    if file_extension in extension_folders:
        # Create the folder if it doesn't exist
        folder_path = os.path.join(directory, extension_folders[file_extension])
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Move the file to the corresponding folder
        shutil.move(os.path.join(directory, filename), os.path.join(folder_path, filename))

print("Files organized successfully!")