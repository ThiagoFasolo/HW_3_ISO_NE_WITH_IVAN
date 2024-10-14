import panel as pn
from widgets import energy_source_widget, date_range_widget, width_slider, height_slider, category_type_widget  # Import new widget
from callbacks import get_energy_data, get_energy_plot, get_line_graph, get_sankey_diagram  # Assuming you created these callbacks

pn.extension()

# Bind widgets to callback functions
data_table = pn.bind(get_energy_data, energy_source_widget, date_range_widget)
energy_plot = pn.bind(get_energy_plot, energy_source_widget, date_range_widget, width_slider, height_slider)
line_graph = pn.bind(get_line_graph, energy_source_widget, date_range_widget, category_type_widget)  # Pass category type widget
sankey_diagram = pn.bind(get_sankey_diagram, date_range_widget, category_type_widget)  # Pass category type widget

# Define the layout with widgets and the main display components
layout = pn.template.FastListTemplate(
    title="Energy Production Dashboard",
    sidebar=[
        pn.Card(pn.Column(energy_source_widget, date_range_widget, category_type_widget), title="Filters", width=320),  # Add new widget here
        pn.Card(pn.Column(width_slider, height_slider), title="Plot Settings", width=320)
    ],
    main=[
        pn.Tabs(
            ("Energy Data Table", data_table),
            ("Energy Production Plot", energy_plot),
            ("Energy Line Graph", line_graph),  # New tab for the line graph
            ("Energy Sankey Diagram", sankey_diagram)  # New tab for the Sankey diagram
        ),
    ],
    header_background='#1F618D'
).servable()

layout.show()
