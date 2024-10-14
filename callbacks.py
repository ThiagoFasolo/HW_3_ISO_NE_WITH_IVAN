from ISO_API_Request import request_ISO_genfuelmix_daterange
import plotly.express as px
import panel as pn  # Import Panel for UI components
from datetime import datetime

def get_energy_data(energy_source, date_range):
    # Extract start and end dates from the date range widget
    starting_date, ending_date = date_range

    # Convert the start and end dates to the 'YYYYMMDD' format
    starting_date = starting_date.strftime('%Y%m%d')
    ending_date = ending_date.strftime('%Y%m%d')

    # Fetch data using the API with the correctly formatted date range
    df = request_ISO_genfuelmix_daterange(beg_date=starting_date, end_date=ending_date)

    # Filter the data by the selected energy source
    filtered_df = df[df['FuelCategory'] == energy_source]

    # Return the filtered data as a Panel DataFrame component
    return pn.pane.DataFrame(filtered_df, width=800)


def get_energy_plot(energy_source, date_range, plot_width, plot_height):
    # Extract and format start and end dates
    start_date, end_date = date_range
    start_date = start_date.strftime('%Y%m%d')
    end_date = end_date.strftime('%Y%m%d')

    # Fetch and filter data based on the energy source and formatted dates
    df = request_ISO_genfuelmix_daterange(beg_date=start_date, end_date=end_date)
    filtered_df = df[df['FuelCategory'] == energy_source]

    # Generate a Plotly bar plot
    fig = px.bar(
        filtered_df,
        x='FuelCategory',
        y='GenMw',
        title=f"Energy Production for {energy_source}",
        labels={'GenMw': 'Generated MW', 'FuelCategory': 'Fuel Category'},
        width=plot_width,  # Set the width of the plot
        height=plot_height  # Set the height of the plot
    )

    # Return the Plotly figure wrapped in a Panel object for rendering
    return pn.pane.Plotly(fig, width=plot_width, height=plot_height)




