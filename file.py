import subprocess
import re


if __name__=="__main__":
    status_result = subprocess.check_output(["git","status"]).decode()
    print(status_result)
    modified_pattern = r"modified:\s+(.*)"
    #print(re.findall(modified_pattern,status_result))
    all_files = r".*[a-z0-9]+\.\S+"
    found_files = (re.findall(all_files,status_result))
    folders = r"\S*/\s"

    found_folders = re.findall(folders,status_result)
    for file in found_files:
        print(file.strip())
    for folder in found_folders:
        print(folder.strip())
