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

def get_energy_data(df, exclude_energy):
    # Filter the data by the selected energy source
    options = list(set(['Solar', 'Wind', 'Hydro', 'Nat. Gas', 'Ren.']) - set(exclude_energy))
    filtered_df = df[df['FuelCategory'].isin(options)]

    # Return the filtered data as a Panel DataFrame component
    return pn.pane.DataFrame(filtered_df, width=800)

def get_line_graph(df, category_type, exclude_categories, plot_width, plot_height):

    if exclude_categories:
        df = df[~df[category_type].isin(exclude_categories)]

    # Generate the line plot
    fig = line_graph(df, category_type = category_type, width = plot_width, height = plot_height)
    # Return the Plotly figure wrapped in a Panel object for rendering
    return pn.pane.Plotly(fig)

def get_sankey_diagram(df, plot_width, plot_height):
    fig = create_energy_sankey(df, plot_width, plot_height)
    return pn.pane.Plotly(fig)



