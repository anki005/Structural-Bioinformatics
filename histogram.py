import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\Bioinformatics project\dataset\antibodies_rigid.csv")
op_dir = r"D:\Bioinformatics project\Histograms\anti_rigid"


for column in df.columns:
    if column == 'caprieval_rank':
        continue
    else: 
        fig, ax = plt.subplots(figsize=(8, 6))

    # Create histogram
    counts, bins, bars = ax.hist(df[column], bins=10, color='green', alpha=0.4, edgecolor='black')

    # Add counts to each bar
    for bar, count in zip(bars, counts):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 0.5,
                str(int(count)), ha='center', va='bottom', fontsize=10, color='black')

    # Add labels and title
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(axis='both', linestyle='--', alpha=0.7)

    # Save the plot
    file_path = os.path.join(op_dir, f"{column}_histogram.png")
    plt.savefig(file_path)
    plt.close()  # Close the plot to avoid overlap
    print(f"Saved histogram for {column} at {file_path}")





