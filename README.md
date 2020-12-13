#  Glioma Margin Assessment based on <br/>Targeted Metabolomics Analyses 
Source code for "Targeted Metabolomics Analyses for Tumor Margin Assessment During Surgery"<br/>
Doruk Cakmakci, Caroline Bund, Martial Piotto, Izzie Jacques Namer and A. Ercument Cicek

Currently, this repository is under construction.
## Dependencies
- We provide a conda environment (for Ubuntu) which includes the following libraries:
  - Scipy
  - PyTorch
  - Matplotlib
  - Pandas
  - xlsxwriter
  - openpyxl
- In order to process HRMAS NMR spectrum we use [pyNMR](https://github.com/bennomeier/pyNMR) which must be built from source (see Initialization section).
- Dependencies listed below must be installed via pip:
  - shap
  - [sklearn (Development Version)](https://scikit-learn.org/stable/developers/advanced_installation.html).


## Initialization
### Development Environment
- First pyNMR library should be initialized using the following commands:
```
$ cd lib
$ git clone https://github.com/bennomeier/pyNMR
```
- Then the conda environment should be initialized as follows:
```
$ conda env create -f targeted-ng.env.yml
$ conda activate targeted-ng
$ pip install shap
$ pip install --pre --extra-index https://pypi.anaconda.org/scipy-wheels-nightly/simple scikit-learn
```

## Creating CPMG and ERETIC-CPMG Datasets from Raw HRMAS NMR Spectra

## Visualising Samples with t-SNE

## Learning to Predict Metabolite Levels
## Learning to Predict Pathological Classification