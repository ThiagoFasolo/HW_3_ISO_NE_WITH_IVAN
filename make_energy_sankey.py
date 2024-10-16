import pandas as pd
import sandkey

def create_energy_sankey(df, width, height):
    df['Total'] = 'Total'
    col2 = 'FuelCategoryRollup'
    col1 = 'FuelCategory'
    word = 'NonRenewable'

    # # Calculate the total Mw for each FuelCategoryRollup
    # total_mw_df = df.groupby('FuelCategoryRollup')['GenMw'].sum().reset_index()
    #
    # # LOOK HERE
    # # Add a new row for the "Total Generation" level, aggregating by FuelCategoryRollup
    # total_df = pd.DataFrame({
    #     'CategoryRollup': ['Total'] * len(total_mw_df),
    #     'FuelCategoryRollup': total_mw_df['FuelCategoryRollup'],
    #     'GenMw': total_mw_df['GenMw']
    # })

    # # Combine original dataframe with the total generation row
    # df_pairs = df_pairing(df, columns=['CategoryRollup', ])
    # df_concat = pd.concat(df_pairs, axis=0)
    # df_concat = pd.concat([df_concat, total_df], axis=0)

    df[col2] = df.apply(lambda row: word if row[col1] == row[col2] else row[col2], axis=1)

    tot_ren = df[df['FuelCategoryRollup'] == 'Renewables']['GenMw'].sum()
    tot_non_ren = df[df['FuelCategoryRollup'] == 'NonRenewable']['GenMw'].sum()

    tot_ren_row = {'GenMw': tot_ren, 'FuelCategory': 'Renewables', 'FuelCategoryRollup': 'Total'}
    tot_non_ren_row = {'GenMw': tot_non_ren, 'FuelCategory': 'NonRenewable', 'FuelCategoryRollup': 'Total'}
    df = df._append(tot_ren_row, ignore_index=True)
    df = df._append(tot_non_ren_row, ignore_index=True)

    sandkey_fig = sandkey.make_sankey(df, columns=['FuelCategoryRollup', 'FuelCategory'], vals_col='GenMw',  width=width, height=height)

    return sandkey_fig