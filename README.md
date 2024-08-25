This the code for the saving the files in the folder. The files may be JPEG,PNG or pdf etc.<br>
<br>
Here's a brief explanation of the file organization script:Before moving further let us describe in brief about the file organization script:
Import Libraries:
os: As for working with the operating system in questions of communication within it, for instance, to define the files, check the paths, etc.
shutil: In relation to other file operations for example copying files from one directory to another.
Set Directory Path:
directory: The path of the folder in which files are to be stored, and which will store files in categorized manner.
Define Extension-to-Folder Mapping:
extension_folders: A script where the key is the file extension while the value to be formed is the name of the folder in which the extending file type belongs to.
Organize Files:
Loop through Files: The next step we can go further and take the value from the second line and go through each file in the directory.
Get File Extension: Skip the extension (characters after the dot) of the filename, e. g. ‘txt’, ‘pdf’, etc.
Check and Create Folders: Therefore, for each of the file extension – it is needed to check if there is the folder with the similar name and if there is not – create it.
Move Files: This process is engaged in arranging every single file in the particular folder due to the extension that it has.
Completion Message:
However, to ensure that all the files have been successfully organized before printing success message, we have the following:
The script organizes the files in the directory that is specified in the script through using the file extensions of the files.
