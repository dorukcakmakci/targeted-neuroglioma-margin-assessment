import os 
import pickle
import numpy as np 
import pandas as pd
import pdb

# define source and target folders 
project_base_path = "/home/doruk/glioma_quantification/"
source_data_path = os.path.join(project_base_path, "data/eretic/raw/")
target_data_path = os.path.join(project_base_path, "data/eretic/fully_quantified/")

# load source data 
with open(os.path.join(source_data_path, "all_samples_spectra"), "rb") as f:
    all_spectra = pickle.load(f)
with open(os.path.join(source_data_path, "all_samples_quantification"), "rb") as f:
    all_quantification = pickle.load(f)
with open(os.path.join(source_data_path, "all_samples_quantification_availability"), "rb") as f:
    all_quantification_availability = pickle.load(f)
all_statistics = pd.read_pickle(os.path.join(source_data_path, "all_samples_statistics"))


# generate target data 
fully_quantified_idx = np.where(np.mean(all_quantification_availability, axis=1) == 1)[0]
fully_quantified_samples_spectra = all_spectra[fully_quantified_idx,:]
fully_quantified_samples_quantification = all_quantification[fully_quantified_idx,:]
fully_quantified_samples_statistics = all_statistics.iloc[fully_quantified_idx].reset_index(drop=True)

pdb.set_trace()

# save target data 
with open(f"{target_data_path}fully_quantified_samples_spectra", "wb") as f:
    pickle.dump(fully_quantified_samples_spectra, f)
with open(f"{target_data_path}fully_quantified_samples_quantification", "wb") as f:
    pickle.dump(fully_quantified_samples_quantification, f)
fully_quantified_samples_statistics.to_pickle(f"{target_data_path}fully_quantified_samples_statistics")