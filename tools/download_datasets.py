#!/usr/bin/python

import sys

def parse_args():
    arguments = len(sys.argv) - 1
    return arguments

def download_datasets():
    number_of_arguements = parse_args()
    print ("The script is called with %i arguments" % (number_of_arguements))
    return None

if __name__ == "__main__":
   download_datasets()
