import pandas as pd
import ISO_API_Request as isoapi
import plotly.express as px
from datetime import datetime

def line_graph(df, category_type='FuelCategory'):
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
        hovermode='x unified'
    )

    # Show the figure
    fig.show()
def plot_total_energy(beg_date = 20240101, end_date = datetime.now().strftime('%Y%m%d'), category_type = 'FuelCategory'):
    '''
    :param beg_date: Start Date of Graph in YYYYMMDD format
    :param end_date: End Date of Graph in YYYYMMDD format
    :param category_type: Choose either 'FuelCategory' or 'FuelCategoryRollup' for line distinction.
    :return: the specified line graph
    '''
    df = isoapi.request_ISO_genfuelmix_daterange(beg_date, end_date)
    line_graph(df, category_type)