#!/usr/bin/python

import argparse
import zipfile

import kaggle

dataset_list = ["titanic"]


def create_parser():
    parser = argparse.ArgumentParser(description = "An addition program")

    parser.add_argument("--all", action="store_true", required=False,
                        help = "Download all of the datasets for this repository.")

    parser.add_argument("--single", nargs = 1, metavar = "single", type = str, required=False,
                    help = "Download a single dataset for this repository.")

    return parser


def fetch_kaggle_dataset(dataset):
    kaggle.api.competition_download_files(dataset, path=f"./datasets/{dataset}", quiet=False)
    with zipfile.ZipFile(f"./datasets/{dataset}/{dataset}.zip","r") as zip_ref:
        zip_ref.extractall(f"./datasets/{dataset}")
    return None

def parse_args(parser):
    args = parser.parse_args()
    if(args.all == True):
        for dataset in dataset_list:
             fetch_kaggle_dataset(dataset)
        return None
    
    elif(args.single[0] in dataset_list):
        fetch_kaggle_dataset(args.single[0])
        return None
    
    else:
        raise KeyError("Dataset not found. Check the README for supported datasets.") 



def download_datasets():
    parser = create_parser()
    parse_args(parser)
    return None

if __name__ == "__main__":
   download_datasets()
