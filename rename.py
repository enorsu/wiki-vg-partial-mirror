import glob
import os


def rename():
    files = glob.glob("./wikivg/*")

    for x in files:
        new_name = x + ".html"
        command = "mv " + x + " " + new_name
        os.system(command)

rename()
