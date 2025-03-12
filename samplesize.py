import pandas as pd

df1 = pd.read_csv(r"D:\Bioinformatics project\dataset\antibodies_emref.csv")
sample_size1 = df1.shape[0] 
df2 = pd.read_csv(r"D:\Bioinformatics project\dataset\antibodies_rigid.csv")
sample_size2 = df2.shape[0]
df3 = pd.read_csv(r"D:\Bioinformatics project\dataset\nanobodies_emref.csv")
sample_size3 = df3.shape[0]
df4 = pd.read_csv(r"D:\Bioinformatics project\dataset\nanobodies_rigid.csv")
sample_size4 = df4.shape[0] 

print(f"Sample size is : {sample_size1}")
print(f"Sample size is : {sample_size2}")
print(f"Sample size is : {sample_size3}")
print(f"Sample size is : {sample_size4}")