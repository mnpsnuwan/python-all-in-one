import os
import shutil

path = "../../data/test.txt"
empty_folder_path = "../../data/new"
data_folder_path = "../../data"

try:
    # os.remove(path)
    # os.remove(folder_path)  # Cannot delete directory using this
    # os.rmdir(empty_folder_path)  # Delete an empty directory
    shutil.rmtree(data_folder_path)  # Delete a directory containing files
except FileNotFoundError as e:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete")
except OSError:
    print("You cannot delete it using that function")
else:
    # print(path + " was deleted!")
    # print(empty_folder_path + " was deleted!")
    print(data_folder_path + " was deleted!")

