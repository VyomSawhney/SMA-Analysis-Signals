import os
import pandas as pd

def remove_middle_signals(df, column='Signal'):
    df['chain'] = (df[column] != df[column].shift()).cumsum()
    chain_counts = df.groupby('chain').size()
    valid_chains = chain_counts[chain_counts > 1].index
    df['valid_chain'] = df['chain'].isin(valid_chains)
    first_last_df = df.groupby('chain').apply(lambda group: group.iloc[[0, -1] if len(group) > 1 else [0]])
    valid_chains_df = first_last_df[first_last_df['valid_chain']].copy()
    valid_chains_df.reset_index(drop=True, inplace=True)
    valid_chains_df.drop(columns=['chain', 'valid_chain'], inplace=True)
    return valid_chains_df

def remove_NA(df, column='Signal'):
    df = df.dropna(subset=[column])
    return df

file_name = input("Please enter the name of your CSV file: ")

if not file_name.endswith(".csv"):
    file_name += ".csv"
try:
    df = pd.read_csv(file_name)

    df = remove_middle_signals(df, 'Signal')

    df = remove_NA(df, 'Signal')

    file_name_without_extension = os.path.splitext(file_name)[0]

    output_file_name = file_name_without_extension + "_parsed.csv"

    df.to_csv(output_file_name, index=False)

    output_directory = os.path.dirname(os.path.abspath(output_file_name))

    print(f"Processed data saved to {output_file_name} in {output_directory}")

except FileNotFoundError:
    print("File not found. Please make sure the input file exists.")