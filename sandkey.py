import plotly.graph_objects as go
import pandas as pd

pd.set_option('future.no_silent_downcasting', True)


def merge_and_sum_rows(df, col1, col2, col_sum):
    '''
    helper function for df_pairing
    '''
    result = df.groupby([col1, col2])[col_sum].sum().reset_index()
    return result

def make_pairs(lst):
    '''
    helper function for df_pairing
    '''
    result = []
    # create unique pairs without repetition
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            result.append([lst[i], lst[j]])
    return result


def df_pairing(df, columns=['Gender', 'Decade', 'Nationality']):
    '''
    Creates a list of dataframes
    each is a unique combinations of column pairs from the input dataframe df
    grouped and summed by a specified 'Count' column
    '''
    df_pairs_list = []
    column_pairs = make_pairs(columns)
    for pairs in column_pairs:
        col1, col2 = pairs
        df_pairs = merge_and_sum_rows(df, col1, col2, 'Count')
        df_pairs.rename(columns={col1: 'Source', col2: 'Target'}, inplace=True)
        df_pairs_list.append(df_pairs)
    return df_pairs_list


def _code_mapping(df, src, targ):
    """ Map labels in src and targ to integers """
    # get distinct labels
    combined = pd.concat([df[src], df[targ]], axis=0)
    unique_values = pd.unique(combined)
    labels = sorted(unique_values, key=lambda x: (isinstance(x, str), x))

    # get integer codes
    codes = list(range(len(labels)))
    # create label to code mapping
    lc_map = dict(zip(labels, codes))
    # substitute names for codes in the dataframe
    df = df.replace({src: lc_map, targ: lc_map})

    return df, labels


def make_sankey(df, columns=['Gender', 'Decade', 'Nationality'], vals_col=None, **kwargs):
    """
    Create a sankey figure
    df - Dataframe
    columns - columns for source and target
    (order cols by source then targets)
    vals_col - column name of values (thickness)
    """

    if vals_col == 'Count':
        pass
    elif vals_col:
        df['Count'] = df[vals_col]
    else:
        values = [1] * len(df)
        df['Count'] = values

    df_pairs = df_pairing(df, columns=columns)
    df_concat = pd.concat(df_pairs, axis=0)

    df, labels = _code_mapping(df_concat, 'Source', 'Target')
    link = {'source': df["Source"], 'target': df["Target"], 'value': df["Count"]}

    thickness = kwargs.get("thickness", 50)  # 50 is the presumed default value
    pad = kwargs.get("pad", 50)

    node = {'label': labels, 'thickness': thickness, 'pad': pad}

    sk = go.Sankey(link=link, node=node)
    fig = go.Figure(sk)
    fig.show()