import ISO_API_Request as isoapi
import plotly.express as px
from datetime import datetime
import sandkey

def line_graph(df, category_type='FuelCategory', width = 500, height =800):
    """
    Parameters:
    - df: A DataFrame containing columns 'BeginDate', 'GenMw', and fuel category columns.
    - category_type: Choose either 'FuelCategory' or 'FuelCategoryRollup' for line distinction.
    """

    fig = px.line(df,
                  x='BeginDate',
                  y='GenMw',
                  color=category_type,  # Group by the chosen fuel category
                  labels={'BeginDate': 'Day/Time', 'GenMw': 'Generation (MW)'},
                  title=f'Generation by {category_type}')

    # Update layout for better visibility
    fig.update_layout(
        xaxis_title='Day/Time',
        yaxis_title='Generation (MW)',
        legend_title=category_type,
        hovermode='x unified',
        width=width,
        height=height
    )

    return fig

def plot_total_energy(beg_date = 20240101, end_date = datetime.now().strftime('%Y%m%d'), category_type = 'FuelCategory'):
    '''
    :param beg_date: Start Date of Graph in YYYYMMDD format
    :param end_date: End Date of Graph in YYYYMMDD format
    :param category_type: Choose either 'FuelCategory' or 'FuelCategoryRollup' for line distinction.
    :return: the specified line graph
    '''
    df = isoapi.request_ISO_genfuelmix_daterange(beg_date, end_date)
    fig = line_graph(df, category_type)

    return fig

def create_energy_sankey(df, width, height):
    df['Total'] = 'Total'
    col2 = 'FuelCategoryRollup'
    col1 = 'FuelCategory'
    word = 'NonRenewable'

    df[col2] = df.apply(lambda row: word if row[col1] == row[col2] else row[col2], axis=1)

    tot_ren = df[df['FuelCategoryRollup'] == 'Renewables']['GenMw'].sum()
    tot_non_ren = df[df['FuelCategoryRollup'] == 'NonRenewable']['GenMw'].sum()

    tot_ren_row = {'GenMw': tot_ren, 'FuelCategory': 'Renewables', 'FuelCategoryRollup': 'Total'}
    tot_non_ren_row = {'GenMw': tot_non_ren, 'FuelCategory': 'NonRenewable', 'FuelCategoryRollup': 'Total'}
    df = df._append(tot_ren_row, ignore_index=True)
    df = df._append(tot_non_ren_row, ignore_index=True)

    sandkey_fig = sandkey.make_sankey(df, columns=['FuelCategoryRollup', 'FuelCategory'], vals_col='GenMw',  width=width, height=height)

    return sandkey_fig