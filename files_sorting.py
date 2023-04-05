import os
import shutil
import tkinter as tk
from tkinter import filedialog


def create_folders(path):
    """
    This function takes in a path and creates a folder for each file extension found in the given path.
    """
    files = os.listdir(path)
    extensions = set([os.path.splitext(file)[1] for file in files])

    for ext in extensions:
        folder_name = ext[1:]  # remove the leading dot from the extension
        folder_path = os.path.join(path, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    return extensions


def sort_files(path, extensions):
    """
    This function takes in a path and a list of file extensions and sorts all the files with those extensions
    into the corresponding folder.
    """
    for ext in extensions:
        folder_name = ext[1:]  # remove the leading dot from the extension
        folder_path = os.path.join(path, folder_name)

        for file in os.listdir(path):
            if file.endswith(ext):
                file_path = os.path.join(path, file)
                shutil.move(file_path, folder_path)


def select_folder():
    """
    This function uses the tkinter library to open a dialog box and ask the user to select a folder.
    """
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    return folder_path


def main():
    # Ask the user to select a folder
    path = select_folder()

    # Create folders for each file extension found in the folder
    extensions = create_folders(path)

    # Sort the files into the corresponding folder
    sort_files(path, extensions)

    print("Done sorting files.")


if __name__ == '__main__':
    main()
