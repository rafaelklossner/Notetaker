import argparse
import datetime
import os

print("---------- NoteTaker ----------")

parser = argparse.ArgumentParser(description='Notetaker')
parser.add_argument('-f','--file', default='demoFileName', help='Name of the file', required=True)
parser.add_argument('--header', action='store_true')
args = vars(parser.parse_args())

file_name = args["file"]
print("Open file " + args["file"])

if not os.path.isfile(file_name + ".md"):
    file = open(file_name + ".md", "w")

    if args["header"]:
        file.write("# " + file_name + "\n" + "\n")
        file.write("<sup> Created by Rafael Klossner on " + str(datetime.datetime.now()) + " </sup>" + "\n")

    file.close()

os.system("code " + file_name + ".md")
