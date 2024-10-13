from ISO_API_Request import request_ISO_genfuelmix_daterange
import panel as pn  # Import Panel for UI components

def get_energy_data(energy_source, date_range):
    # Extract start and end dates from the date range widget
    start_date, end_date = date_range

    # Convert the start and end dates to the 'YYYYMMDD' format
    start_date = start_date.strftime('%Y%m%d')
    end_date = end_date.strftime('%Y%m%d')

    # Fetch data using the API with the correctly formatted date range
    df = request_ISO_genfuelmix_daterange(beg_date=start_date, end_date=end_date)

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

    # Generate a plot (for example, a bar plot using Plotly or Matplotlib)
    fig = filtered_df.plot(kind='bar', x='FuelCategory', y='GenMw', figsize=(plot_width, plot_height))

    return pn.pane.Matplotlib(fig, width=plot_width, height=plot_height)


