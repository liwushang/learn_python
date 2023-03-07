# -*-coding:utf-8-*-

import os
import sys
def File_back(file_path):
    with open(file_path) as fin:
        root, filename = os.path.split(file_path)
        filenameback = str(root)+str(filename) + ".back"
        ff = fin.read()
        with open(filenameback, "w") as fout:
            fout.write(ff)

def Handle_string(file_path):

    with open(file_path) as fin:
        lines = fin.readlines()
        for line in lines:
            line_head = line[:98]+"'"
            if line[98:] is not None:
                line_end = "'" + line[98:]
            print(line_head, line_end)


File_back("./handle100.txt")
Handle_string("handle100.txt")

