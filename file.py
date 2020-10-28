import subprocess
import re


if __name__=="__main__":
    status_result = subprocess.check_output(["git","status"]).decode()
    # print(status_result)
    all_files = r".*[a-z0-9]+\.\S+"
    found_files = re.findall(all_files,status_result)
    folders = r"\S*/\s"

    found_folders = re.findall(folders,status_result)
    # for file_name in found_files:
    #     print(file_name.strip())
    # for folder_name in found_folders:
    #     print(folder_name.strip())
    modified = list()
    untracked = list()
    for file_name in found_files:
        if "modified" in file_name:
            file_name = re.findall(r"modified:[\s]+(.*)",file_name)[0]
            modified.append(file_name.strip())
        else:
            untracked.append(file_name.strip())
    for folder_name in found_folders:
        if "modified" in folder_name:
            folder_name = re.findall(r"modified:[\s]+(.*)",folder_name)[0]
            modified.append(folder_name.strip())
        else:
            untracked.append(folder_name.strip())
    print(f"modified={modified}\nuntracked={untracked}")
    #code to fetch the first lineof modified files
    for fil in modified:
    	with open(fil) as f:
    		first_line = f.readline()
    		print(first_line)