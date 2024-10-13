# dashboard_template.py
import panel as pn
from widgets import energy_source_widget, date_range_widget, update_interval_widget, width_slider, height_slider
from callbacks import get_energy_data, get_energy_plot

pn.extension()

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
            ("Energy Data Table", get_energy_data()),  # Actual callback from callback script
            ("Energy Production Plot", get_energy_plot()),  # Actual plot callback
        ),
    ],
    header_background='#1F618D'  # Professional header color
).servable()

layout.show()
