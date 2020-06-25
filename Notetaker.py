import datetime
import os
from ConfigParser import ConfigParser
from ArgParser import ArgParser


def create_file(file_name, is_header, path, is_author):
    print("Create new file: " + file_name)
    file = open(path + file_name, "w")
    if is_header:
        print("Add header to file")
        file.write("# " + file_name + "\n" + "\n")
        if is_author:
            file.write("<sup> Created by Rafael Klossner on " + str(datetime.datetime.now()) + " </sup>" + "\n")
    file.close()


def open_file_with_editor(file_name, editor, path):
    print("Open file " + file_name)
    os.system(editor + " " + path + file_name)


def main():
    arg_parser = ArgParser()
    config_parser = ConfigParser()

    file_name = arg_parser.file_name + '.md'
    is_header = arg_parser.header
    path = config_parser.get_settings_value("default_path") + "/"
    editor = config_parser.get_settings_value('editor')
    is_author = config_parser.get_header_value('author')

    print("---------- NoteTaker ----------")

    if not os.path.exists(path):
        print("Create new path: " + path)
        os.makedirs(path)

    if not os.path.isfile(path + arg_parser.file_name):
        create_file(file_name, is_header, path, is_author)

    open_file_with_editor(file_name, editor, path)


if __name__ == '__main__':
    main()
