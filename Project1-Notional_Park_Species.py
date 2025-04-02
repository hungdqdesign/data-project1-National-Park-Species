import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as sns  
  
input_file = 'most_visited_nps_species_data.csv'  
output_file = 'most_visited_nps_species_data_tidy_keep_first.csv'  
df = pd.read_csv(input_file, encoding='latin-1')  
  
df.columns = [col.strip() for col in df.columns]  
  
columns_to_process = ['CommonNames', 'ParkTags', 'ExternalLinks', 'StateStatus', 'OzoneSensitiveStatus']  
  
for col in columns_to_process:  
    if col in df.columns:  
        df[col] = df[col].apply(  
            lambda x: str(x).split(',')[0].strip() if pd.notna(x) else np.nan  
        )  
  
for col in df.select_dtypes(include=['object']).columns:  
    df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)  
  
df = df.fillna('N/A')  
  
df.to_csv(output_file, index=False, encoding='utf-8')  
  
print(f'Rows in original file: {pd.read_csv(input_file, encoding="latin-1").shape[0]}')  
print(f'Rows in tidy file: {df.shape[0]}')  
print(f'Columns in tidy file: {df.shape[1]}')  
  
print("\nFirst 5 rows of tidy data:")  
print(df.head())