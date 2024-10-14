from ISO_API_Request import request_ISO_genfuelmix_daterange
import panel as pn
from make_energy_sankey import create_energy_sankey
from make_energy_linecharts import line_graph

def fetch_data(date_range):
    # Convert the date range
    start_date, end_date = date_range
    start_date = start_date.strftime('%Y%m%d')
    end_date = end_date.strftime('%Y%m%d')

    # Generate the Sankey diagram using the selected category type
    df = request_ISO_genfuelmix_daterange(beg_date=start_date, end_date=end_date)
    # return pn.pane.Plotly(fig)
    return df

def get_energy_data(df, energy_source):
    # Filter the data by the selected energy source
    filtered_df = df[df['FuelCategory'] == energy_source]

    # Return the filtered data as a Panel DataFrame component
    return pn.pane.DataFrame(filtered_df, width=800)

def get_line_graph(df, category_type, plot_width, plot_height):
    # Generate the line plot
    fig = line_graph(df, category_type = category_type, width = plot_width, height = plot_height)
    # Return the Plotly figure wrapped in a Panel object for rendering
    return pn.pane.Plotly(fig)

def get_sankey_diagram(df):
    fig = create_energy_sankey(df)
    return pn.pane.Plotly(fig)



