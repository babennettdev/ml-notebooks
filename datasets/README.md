# Datasets

## Manual Download

You can download datasets directly from Kaggle.com. Folder structure (to ensure no modifications are necessary) is listen below.

```
datasets 
|--- {dataset_name}
    |--- {dataset_name}.zip
    |--- *.csv
```

## CLI Tool

### CLI Tool Installation
Register for an account on Kaggle.com and follow their [Authentication instructions](https://www.kaggle.com/docs/api). Ensure the API key is stored properly.

Install the necessary packages by executing the following command from the root directory:

```
pip install -r .\tools\requirements.txt
```

Now you should be ready to run the CLI tool to download datasets!

### CLI Tool Download
To download all datasets, run the following command from the root directory:

```
python .\tools\download_datasets.py --all
```

To download a single dataset, run the following command from the root directory:

```
python .\tools\download_datasets.py --single {dataset_name}
```
