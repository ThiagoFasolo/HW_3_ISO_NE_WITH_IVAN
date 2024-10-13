import panel as pn

# Loads javascript dependencies and configures Panel (required)
pn.extension()

# WIDGET DECLARATIONS
energy_source_widget = pn.widgets.Select(name="Energy Source", options=['Solar', 'Wind', 'Hydro', 'Gas'], value='Solar')
date_range_widget = pn.widgets.DateRangePicker(name="Date Range", start='2022-01-01', end='2022-12-31')
update_interval_widget = pn.widgets.IntSlider(name="Update Interval (Minutes)", start=1, end=60, step=1, value=10)

# Plotting widgets
width_slider = pn.widgets.IntSlider(name="Plot Width", start=300, end=2000, step=100, value=1200)
height_slider = pn.widgets.IntSlider(name="Plot Height", start=300, end=1500, step=100, value=800)

# CALLBACK FUNCTIONS
def get_energy_data():
    # Example callback to retrieve energy data; replace with actual data processing
    return pn.widgets.Tabulator(value=[
        {'Energy Source': 'Solar', 'Production (MW)': 500, 'Date': '2022-05-01'},
        {'Energy Source': 'Wind', 'Production (MW)': 300, 'Date': '2022-05-02'},
    ], selectable=False)

def get_energy_plot():
    # Example plot; replace with actual plot logic using energy data
    return pn.pane.Markdown("![Energy Plot](https://via.placeholder.com/1500x800)", height=800)

# Cards and Layout
filter_card = pn.Card(
    pn.Column(
        energy_source_widget,
        date_range_widget,
        update_interval_widget
    ),
    title="Filters", width=320, collapsed=False, header_color="#5DADE2"
)

plot_card = pn.Card(
    pn.Column(
        width_slider,
        height_slider
    ),
    title="Plot Settings", width=320, collapsed=True, header_color="#5DADE2"
)

# Main Layout with Tabs
layout = pn.template.FastListTemplate(
    title="Energy Production Dashboard",
    sidebar=[
        filter_card,
        plot_card,
    ],
    theme_toggle=True,
    main=[
        pn.Tabs(
            ("Energy Data Table", get_energy_data()),  # Mockup table callback
            ("Energy Production Plot", get_energy_plot()),  # Mockup plot callback
        ),
    ],
    header_background='#1F618D'  # Darker blue for a professional look
).servable()

layout.show()
