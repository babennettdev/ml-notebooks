#!/usr/bin/python

import argparse

dataset_list = ["titanic"]

def create_parser():
    parser = argparse.ArgumentParser(description = "An addition program")

    parser.add_argument("--all", action="store_true", required=False,
                        help = "Download all of the datasets for this repository.")

    parser.add_argument("--single", nargs = 1, metavar = "single", type = str, required=False,
                    help = "Download a single dataset for this repository.")

    return parser
    

def parse_args(parser):
    args = parser.parse_args()
    if(args.all == True):
        return None
    
    elif(args.single in dataset_list):
        return None



def download_datasets():
    parser = create_parser()
    parse_args(parser)
    return None

if __name__ == "__main__":
   download_datasets()
