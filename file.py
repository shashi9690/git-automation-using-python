import subprocess
import re


if __name__=="__main__":
    status_result = subprocess.check_output(["git","status"]).decode()
    print(status_result)
