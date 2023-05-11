import os
import shutil
import glob

def delete_folders_by_pattern(path, patterns):
    if not os.path.exists(path):
        return

    for pattern in patterns:
        for directory in glob.glob(os.path.join(path, pattern)):
            try:
                shutil.rmtree(directory)
                print(f"Deleted folder: {directory}")
            except Exception as e:
                print(f"Error deleting folder '{directory}': {e}")

def main():
    folder_name_patterns = ["ProjectNotify*", "ProjectMatrixDataSyncServ_Url_*"]
    locations = [
        os.path.expandvars("%LOCALAPPDATA%\\ProjectMatrix"),
        "C:\\Windows\\System32\\config\\systemprofile\\AppData\\Local\\ProjectMatrix"
    ]

    for location in locations:
        delete_folders_by_pattern(location, folder_name_patterns)

if __name__ == "__main__":
    main()
