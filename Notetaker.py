import argparse
import datetime
import os

print("---------- NoteTaker ----------")

parser = argparse.ArgumentParser(description='Notetaker')
parser.add_argument('--header', action='store_true')
args = vars(parser.parse_args())
print(args["header"])

print("Enter file name: ")
file_name = input()

if not os.path.isfile(file_name + ".md"):
    file = open(file_name + ".md", "w")

    if args["header"]:
        file.write("# " + file_name + "\n" + "\n")
        file.write("<sup> Created by Rafael Klossner on " + str(datetime.datetime.now()) + " </sup>" + "\n")

    file.close()

os.system("code " + file_name + ".md")