import ISO_API_Request as isoapi
import sandkey

def create_energy_sankey(df):
    col2 = 'FuelCategoryRollup'
    col1 = 'FuelCategory'
    word = 'NonRenewable'
    df[col2] = df.apply(lambda row: word if row[col1] == row[col2] else row[col2], axis=1)
    sandkey_fig = sandkey.make_sankey(df, columns=['FuelCategoryRollup', 'FuelCategory'], vals_col='GenMw')

    return sandkey_fig