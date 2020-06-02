import datetime
import os

print("---------- NoteTaker ----------")

print("Enter file name: ")
file_name = input()

if not os.path.isfile(file_name + ".md"):
    file = open(file_name + ".md", "w")
    file.write("# " + file_name + "\n" + "\n")
    file.write("<sup> Created by Rafael Klossner on " + str(datetime.datetime.now()) + " </sup>" + "\n")
    file.close()

os.system("code " + file_name + ".md")