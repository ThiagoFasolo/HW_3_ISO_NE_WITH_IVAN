import plotly.graph_objects as go
import pandas as pd
from pandas import json_normalize

pd.set_option('future.no_silent_downcasting', True)


# Merge and sum rows helper function
def merge_and_sum_rows(df, col1, col2, col_sum):
    result = df.groupby([col1, col2])[col_sum].sum().reset_index()
    return result


# Helper function to create unique pairs
def make_pairs(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            result.append([lst[i], lst[j]])
    return result


# Create unique combinations of column pairs
def df_pairing(df, columns=['FuelCategoryRollup', 'FuelCategory']):
    df_pairs_list = []
    column_pairs = make_pairs(columns)
    for pairs in column_pairs:
        col1, col2 = pairs
        df_pairs = merge_and_sum_rows(df, col1, col2, 'Count')
        df_pairs.rename(columns={col1: 'Source', col2: 'Target'}, inplace=True)
        df_pairs_list.append(df_pairs)
    return df_pairs_list


# Mapping labels to integers
def _code_mapping(df, src, targ):
    combined = pd.concat([df[src], df[targ]], axis=0)
    unique_values = pd.unique(combined)
    labels = sorted(unique_values, key=lambda x: (isinstance(x, str), x))
    codes = list(range(len(labels)))
    lc_map = dict(zip(labels, codes))
    df = df.replace({src: lc_map, targ: lc_map})
    return df, labels


# Modified make_sankey function to include the "Total Mw" level
def make_sankey(df, columns=['FuelCategoryRollup', 'FuelCategory'], vals_col=None, **kwargs):
    # Create Count column based on the provided values column
    if vals_col == 'Count':
        pass
    elif vals_col:
        df['Count'] = df[vals_col]
    else:
        values = [1] * len(df)
        df['Count'] = values

    # Calculate the total Mw and add a "Total Generation" level
    total_mw = df['GenMw'].sum()

    # Add a new row for the "Total Generation" level
    total_df = pd.DataFrame({
        'Source': ['Total Generation'] * len(df),
        'Target': df['FuelCategoryRollup'],
        'Count': df['GenMw']
    })

    # Combine original dataframe with the total generation row
    df_pairs = df_pairing(df, columns=columns)
    df_concat = pd.concat(df_pairs, axis=0)
    df_concat = pd.concat([df_concat, total_df], axis=0)

    # Map labels to integer codes
    df, labels = _code_mapping(df_concat, 'Source', 'Target')

    # Create Sankey diagram links
    link = {'source': df["Source"], 'target': df["Target"], 'value': df["Count"]}

    # Set up node parameters
    thickness = kwargs.get("thickness", 50)
    pad = kwargs.get("pad", 50)

    node = {'label': labels, 'thickness': thickness, 'pad': pad}

    # Create Sankey diagram
    sk = go.Sankey(link=link, node=node)
    fig = go.Figure(sk)
    fig.show()


