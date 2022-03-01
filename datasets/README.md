# Datasets

## Table Of Contents

- [Datasets](#datasets)
- [Table of Contents](#table-of-contents)
- [Manual Download](#manual-download)
- [CLI Tools](#cli-tools)
    - [CLI Tool(s) Installation](#cli-tools-installation)
    - [Download Using download_datasets.py](#download-using-downloaddatasetspy)
    - [Download using the Kaggle API CLI Tool](#download-using-the-kaggle-api-cli-tool)

## Manual Download

You can download datasets directly from Kaggle.com. Folder structure (to ensure no modifications are necessary) is listed below.

```
datasets 
|--- {dataset_name}
    |--- {dataset_name}.zip
    |--- *.csv
```

## CLI Tools

### CLI Tool(s) Installation
Register for an account on Kaggle.com and follow their [Authentication instructions](https://www.kaggle.com/docs/api). Ensure the API key is stored properly.

Install and unzip the necessary packages by executing the following command from the root directory:

```
pip install -r .\tools\requirements.txt
```

Now you should be ready to run the CLI tool to download datasets!

### Download Using download_datasets.py
To download all datasets, run the following command from the root directory:

```
python .\tools\download_datasets.py --all
```

To download a single dataset, run the following command from the root directory:

```
python .\tools\download_datasets.py --single {dataset_name}
```

### Download using the Kaggle API CLI Tool

To download datasets using the Kaggle CLI tool, follow the instructions on their [website](https://www.kaggle.com/docs/api). Datasets should follow the following directory structure to work with this repository's Jupyter Notebooks (without modification).

```
datasets 
|--- {dataset_name}
    |--- {dataset_name}.zip
    |--- *.csv
```