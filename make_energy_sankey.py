import ISO_API_Request as isoapi
import sandkey
from Basic_Table import create_table
from datetime import datetime

def create_energy_sankey(beg_date = 20240101, end_date = datetime.now().strftime('%Y%m%d')):
    df = isoapi.request_ISO_genfuelmix_daterange(beg_date, end_date)
    col2 = 'FuelCategoryRollup'
    col1 = 'FuelCategory'
    word = 'NonRenewable'

    df[col2] = df.apply(lambda row: word if row[col1] == row[col2] else row[col2], axis=1)
    sandkey_fig = sandkey.make_sankey(df, columns=['FuelCategoryRollup', 'FuelCategory'], vals_col='GenMw')

    return sandkey_fig