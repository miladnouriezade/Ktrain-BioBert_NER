# Ktrain BioBert_NER
This repository contains data and BioBert based NER model `monologg/biobert_v1.1_pubmed` from [community-uploaded Hugging Face models](https://huggingface.co/models) for detecting entities such as chemical and disease.

### Setting up an environment
1.  [Follow the installation instructions for Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html?highlight=conda#regular-installation).
2. Create a Conda environment called "Ktrain_NER" with Python 3.7.0:
    ```bash
    conda create -n Ktrain_NER python=3.7.0
    ```
3. Activate the Conda environment:

    ```bash
    conda activate Ktrain_NER
    ```
## Installation
Install required packages .
```sh
$ pip install tensorflow==2.1.0
```
```sh
$ pip install pytorch
```
```sh
$ pip install ktrain
```

## Preparation
## Dataset
Download dataset provided in data folder(BC5CDR-IOB), locate it in any directory you want and address `TRAIN_DATA` and `VALIDATION_DATA` in `parameters.py` .
Use `train-dev.tsv` for training and `test.tsv` for validation.
> Ktrain can use both `validation` and `train` datas or just `train`.

## Train and validate model
Use `python run_ner.py` to train and validate model.