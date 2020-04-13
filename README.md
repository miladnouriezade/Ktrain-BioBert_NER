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

## Learning rate hyper-parameter
We used `lr_find()` to find optimal learning rate. optimal lr is approximately 1e-3 .
<img src="https://gitlab.com/nlp-projects/ktrain/pic/lr_find.png" width="600" height="400" />


## Train and validate model
Use `python run_ner.py` to train and validate model.

# Result
We got the best result using SGDR learning rate scheduler on `BC5CDR-IOB` with `lr=1e-3`,`n_cycles=3`, `cycle_len=1` and `cycle_mult=2`. weights are availabel in `weights` folder.
<img src="https://gitlab.com/nlp-projects/ktrain/pic/SGDR.png" width="600" height="400" />
| | precision  | recall  | f1-score  | support  |
|---|---|---|---|---|
|  Chemical | 0.91  | 091  |  0.91 |5385
| Disease  |  0.75 | 0.81  |  0.78 |4424
| micro avg  | 0.83  | 0.87  | 0.85  |9809
| macro avg  |  0.84 | 0.87  | 0.85  |9809

## Result using fastText
We used `crawl-300d-2M-subword` from [fastext pre-trained word vectors](https://fasttext.cc/docs/en/english-vectors.html) instead of randomly initialized word embeddings with the same parameters and data as before .
| | precision  | recall  | f1-score  | support  |
|---|---|---|---|---|
|  Disease | 0.76  | 0.79  |  0.77 |4424
|  Chemical |  0.91 | 0.89  |  0.90 |5385
| micro avg  | 0.84  | 0.85  | 0.84  |9809
| macro avg  |  0.84 | 0.85  | 0.85  |9809

## Result using fastText and BILOU schemed data
In this expriment we used `BC5CDR-BILOU` _ BILOU schemed data set instead of IOB with `crawl-300d-2M-subword`(fastText word vector) and same parameters.
| | precision  | recall  | f1-score  | support  |
|---|---|---|---|---|
|  Chemical | 0.91  | 0.74  |  0.82 |5374
|  Disease |  0.74 | 0.72  |  0.73 |4397
| micro avg  | 0.83  | 0.73  | 0.78  |9771
| macro avg  |  0.83 | 0.73  | 0.78  |9771
