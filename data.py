import os
import pandas as pd

inp_file = r"D:\Bioinformatics project\dataset\nanobodies_rigid_all.tsv"
out_file = r"D:\Bioinformatics project\dataset\nanobodies_rigid.csv"

df = pd.read_csv(inp_file, sep="\t")
columns = ['vdw', 'elec', 'bsa', 'desolv', 'fnat', 'dockq', 'caprieval_rank', 'Molecule name']

extracted_df = df[columns]

# Save the extracted data to a CSV file
extracted_df.to_csv(out_file, index=False)
print("Done!!!")