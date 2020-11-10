import random 
import os
import pdb 
import pickle
import numpy as np 
import pandas as pd 

project_base_path = "/home/doruk/glioma_quantification/"
import sys 
sys.path.insert(1,os.path.join(project_base_path, "data/"))
from preprocessing_utils import preprocess_spectrum
dataset_excel_path = os.path.join(project_base_path, "data/all_eretic_hrmas_dataset.xlsx")
target_dataset_excel_path = os.path.join(project_base_path, "data/eretic/eretic_cpmg_final_dataset.xlsx")
with open("./valid_eretic_sample_filenames", "rb") as f:
    target_sample_filenames = pickle.load(f)

# read excel sheets to pandas dataframe
statistics_df = pd.read_excel(dataset_excel_path, sheet_name="Tissue Sample Collection")
quantification_df = pd.read_excel(dataset_excel_path, sheet_name="Metabolite Quantifications")
statistics_df["Pathologic Classification"] = statistics_df["Pathologic Classification"].replace("Control ", "Control")

# find the used samples from the dataset according to spectrum filenames
index = statistics_df.index
condition = statistics_df["Spectrum Filename"].isin(target_sample_filenames)
dataset_indices = index[condition].tolist()
statistics = statistics_df.iloc[dataset_indices, :].reset_index(drop=True)
quant = quantification_df.iloc[dataset_indices, :].reset_index(drop=True)

# drop relevant columns and save dataset
statistics_dataset = statistics.drop(labels=["Availability", "Recidive", "Tumor Location", "Cellularity", "Necrosis", "Infiltration (Left)", "Infiltration (Right)", "Date of Death", "Date of Last Control", "Overall Survival (days)", "Metabolite Quantification Filename"], axis="columns")

# write datasets
writer = pd.ExcelWriter(target_dataset_excel_path)
statistics_dataset.to_excel(writer, sheet_name="ERETIC-CPMG Dataset Statistics", na_rep="*", header=True, index=True)
quant.to_excel(writer, sheet_name="ERETIC-CPMG Dataset Metabolites", na_rep="*", header=True, index=True)
writer.save()

pdb.set_trace()