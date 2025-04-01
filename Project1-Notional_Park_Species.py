import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define the tidy_data function
def tidy_data(input_file, output_file):
    df = pd.read_csv(input_file, encoding='latin-1')
    
    #Clean column names
    df.columns = [col.strip() for col in df.columns]
    
    #Split CommonNames by comma and create separate rows
    if 'CommonNames' in df.columns:
        # Convert non-null values to lists of names
        df['CommonNames'] = df['CommonNames'].apply(
            lambda x: [name.strip() for name in str(x).split(',')] if pd.notna(x) else np.nan
        )
        
        #Create a separate row for each name
        df = df.explode('CommonNames')
    
    #Remove whitespace from text columns
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)
    
    #Save the tidy data
    df.to_csv(output_file, index=False, encoding='utf-8')
    
    return df

# Set input and output file paths
input_file = 'most_visited_nps_species_data.csv'
output_file = 'most_visited_nps_species_data_tidy.csv'

# Run the tidy_data function
tidy_df = tidy_data(input_file, output_file)

# Compare original and tidy data
original_df = pd.read_csv(input_file, encoding='latin-1')
print(f'Rows in original file: {original_df.shape[0]}')
print(f'Rows in tidy file: {tidy_df.shape[0]}')
print(f'Columns in tidy file: {tidy_df.shape[1]}')

# Display the first few rows of the tidy data
print("\nFirst 5 rows of tidy data:")
print(tidy_df.head())
