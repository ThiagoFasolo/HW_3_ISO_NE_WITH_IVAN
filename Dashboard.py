import panel as pn
from widgets import exclude_energy_source_widget, date_range_widget, width_slider, height_slider, category_type_widget
from callbacks import get_energy_data, get_line_graph, get_sankey_diagram, fetch_data

# Reactive DataFrame bound to widgets
main_data_frame = pn.bind(fetch_data, date_range_widget)

# Bind widgets to callback functions
data_table = pn.bind(get_energy_data, main_data_frame, exclude_energy_source_widget)
line_graph = pn.bind(get_line_graph, main_data_frame, category_type_widget, exclude_energy_source_widget, width_slider, height_slider)
sankey_diagram = pn.bind(get_sankey_diagram, main_data_frame,  width_slider, height_slider)

# Define the layout with widgets and the main display components
layout = pn.template.FastListTemplate(
    title="Energy Production Dashboard",
    sidebar=[
        pn.Card(pn.Column(exclude_energy_source_widget), title="Exclude Sources", width=320),
        pn.Card(pn.Column(date_range_widget, category_type_widget), title="Filters", width=320),  # Add new widget here
        pn.Card(pn.Column(width_slider, height_slider), title="Plot Settings", width=320)
    ],
    main=[
        pn.Tabs(
            ("Energy Data Table", data_table),
            ("Energy Line Graph", line_graph),  # New tab for the line graph
            ("Energy Sankey Diagram", sankey_diagram)  # New tab for the Sankey diagram
        ),
    ],
    header_background='#1F618D'
).servable()

layout.show()