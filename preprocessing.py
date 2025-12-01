import pandas as pd
import os

# Define the file paths and the specific columns to keep from each
data_specs = {
    "DEMO": {
        "path": "data/DEMO_L.xpt",
        "cols": ["SEQN", "RIAGENDR", "RIDAGEYR", "RIDRETH3", "DMDHHSIZ", "INDFMPIR"]
    },
    "SLQ": {
        "path": "data/SLQ_L.xpt",
        "cols": ["SEQN", "SLD012", "SLD013"]
    },
    "PAQ": {
        "path": "data/PAQ_L.xpt",
        "cols": ["SEQN", "PAD790Q", "PAD790U", "PAD800", "PAD810Q", "PAD810U", "PAD820"]
    },
    "DPQ": {
        "path": "data/DPQ_L.xpt",
        "cols": ["SEQN", "DPQ050", "DPQ020"]
    },
    "ALQ": {
        "path": "data/ALQ_L.xpt",
        "cols": ["SEQN", "ALQ111"]
    },
    "OCQ": {
        "path": "data/OCQ_L.xpt",
        "cols": ["SEQN", "OCD150"]
    }
}

def load_nhanes_data():
    # 1. Load Demographics first to establish the base population (18+)
    print(f"Loading {data_specs['DEMO']['path']}...")
    try:
        demo_df = pd.read_sas(data_specs['DEMO']['path'])
    except FileNotFoundError:
        print(f"Error: Could not find {data_specs['DEMO']['path']}")
        return None

    # Filter for adults (18+)
    initial_count = len(demo_df)
    demo_df = demo_df[demo_df['RIDAGEYR'] >= 18]
    print(f"Filtered DEMO: {initial_count} -> {len(demo_df)} rows (keeping 18+ only)")
    
    demo_df = demo_df[data_specs['DEMO']['cols']]

    # Initialize the final dataset with the filtered demographics data
    final_df = demo_df

    # 2. Iterate through the rest of the files, load, and merge
    file_keys = ["SLQ", "PAQ", "DPQ", "ALQ", "OCQ"]
    
    for key in file_keys:
        spec = data_specs[key]
        path = spec['path']
        cols = spec['cols']
        
        print(f"Loading {path}...")
        try:
            temp_df = pd.read_sas(path)
            
            # Select only specified columns (ensure SEQN is included for merging)
            available_cols = [c for c in cols if c in temp_df.columns]
            if len(available_cols) < len(cols):
                missing = set(cols) - set(available_cols)
                print(f"Warning: Missing columns {missing} in {path}")
            
            temp_df = temp_df[available_cols]
            
            # 3. Inner Join on SEQN
            # 'inner' ensures we only keep rows that exist in BOTH the current result and the new file
            final_df = pd.merge(final_df, temp_df, on="SEQN", how="inner")
            
            print(f"Merged {key}. Current dataset size: {len(final_df)} rows")
            
        except FileNotFoundError:
            print(f"Error: File {path} not found. Skipping...")
        except Exception as e:
            print(f"Error processing {key}: {e}")

    return final_df

if __name__ == "__main__":
    # Create the dataset
    df = load_nhanes_data()

    if df is not None:
        # distinct check to ensure SEQN is unique (it should be)
        print("\nFinal Dataset Info:")
        print(df.info())
        print(df.head())
        
        df.to_csv("data/nhanes_2021_2023_adults_combined.csv", index=False)
        print("Saved to nhanes_2021_2023_adults_combined.csv")