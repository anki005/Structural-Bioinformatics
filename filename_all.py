import pandas as pd
import os
import glob

# Path to the directory containing your files
path = r"D:\Bioinformatics project\Separated capri_data\nanobodies\rigid\*.tsv"

# Get all CSV files in the directory
file_list = glob.glob(path)
#print(file_list)
# Initialize a list to store data from all files
all_data = []

for file_name in file_list:
    # Read each file
    df = pd.read_csv(file_name, sep='\t')
    file = os.path.basename(file_name)
    
    # Add the file name (only the base name, not the full path)
    df["Molecule name"] = file   
    # Append to the list
    all_data.append(df)

# Combine all DataFrames into one
final_df = pd.concat(all_data, ignore_index=True)

# Save the combined DataFrame to a new CSV file
final_df.to_csv(r"D:\Bioinformatics project\dataset\nanobodies_rigid_all.tsv", sep="\t", index=False)


