import panel as pn
from widgets import energy_source_widget, date_range_widget, width_slider, height_slider
from callbacks import get_energy_data, get_energy_plot

pn.extension()

# Bind widgets to callback functions
data_table = pn.bind(get_energy_data, energy_source_widget, date_range_widget.value)
energy_plot = pn.bind(get_energy_plot, energy_source_widget, date_range_widget.value, width_slider, height_slider)

# Define the layout with widgets and the main display components
layout = pn.template.FastListTemplate(
    title="Energy Production Dashboard",
    sidebar=[
        pn.Card(pn.Column(energy_source_widget, date_range_widget), title="Filters", width=320),
        pn.Card(pn.Column(width_slider, height_slider), title="Plot Settings", width=320)
    ],
    main=[
        pn.Tabs(
            ("Energy Data Table", data_table),
            ("Energy Production Plot", energy_plot)
        ),
    ],
    header_background='#1F618D'
).servable()

layout.show()
