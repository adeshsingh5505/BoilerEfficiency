import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = 'boiler_data_with_efficiency.csv'
df = pd.read_csv(file_path)

universal_column = 'Boiler Efficiency (%)'
columns_to_plot = ['Flue gas temperature at the upper economizer outlet (left)', 'Flue gas temperature at the upper economizer outlet (right)', 'Upper economiser inlet flue gas oxygen (left)', 'Upper economiser inlet flue gas oxygen (right)', 'Main steam flow rate after compensation']

all_columns = [universal_column] + columns_to_plot
for col in all_columns:
    if col not in df.columns:
        raise ValueError(f"Column '{col}' not found in CSV.")

output_folder = "individual_plots"
os.makedirs(output_folder, exist_ok=True)

for col in columns_to_plot:
    plt.figure(figsize=(10, 5))
    plt.plot(df[universal_column], df[col], color='blue', linewidth=2)
    plt.xlabel(universal_column)
    plt.ylabel(col)
    plt.title(f"{universal_column} vs {col}")
    plt.grid(True)
    plt.tight_layout()
    filename = os.path.join(output_folder, f"{universal_column}_vs_{col}.png")
    plt.savefig(filename, dpi=300)
    plt.close()
    print(f"Saved: {filename}")