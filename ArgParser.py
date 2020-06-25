import argparse


class ArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Notetaker')
        self.parser.add_argument('-f','--file', default='demoFileName', help='Name of the file', required=True)
        self.parser.add_argument('--header', action='store_true')
        self.arguments = vars(self.parser.parse_args())

        self.file_name = self.arguments['file']
        self.header = self.arguments['header']
