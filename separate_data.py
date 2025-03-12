import pandas as pd
import os
from shutil import move

source = r"D:\Bioinformatics project\capri_data\nanobodies"
destination_emref = r"D:\Bioinformatics project\Separated capri_data\nanobodies\emref"
destination_rigid = r"D:\Bioinformatics project\Separated capri_data\nanobodies\rigid"

for files in os.listdir(source):
    if files.endswith("emref_capri_ss.tsv"):
        move(os.path.join(source, files), os.path.join(destination_emref, files))
    elif files.endswith("rigid_capri_ss.tsv"):
        move(os.path.join(source, files), os.path.join(destination_rigid, files))


