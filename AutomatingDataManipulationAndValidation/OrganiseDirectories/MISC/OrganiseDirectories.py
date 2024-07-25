import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf', '.txt'],
    "AUDIOS": ['.m4a', '.m4b', '.mp3'],
    "VIDEOS": ['.mov', '.avi', '.mp4'],
    "IMAGES": ['.jpg', '.jpeg', '.png']
}


# Choose a directory from the list of subdirectories
def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        if value in suffixes:
            return category
    return "MISC"


# Check if selecting the pdf subdirectory prints out the Documents directory
print(pickDirectory(".pdf"))


# Create a directory path based on the file type
def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = pickDirectory(fileType)
        directoryPath = Path(directory)
        if not directoryPath.is_dir():
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))


# Organise files based on directories
organizeDirectory()
