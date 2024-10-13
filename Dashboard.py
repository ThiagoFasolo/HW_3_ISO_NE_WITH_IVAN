import panel as pn
import pandas as pd
import plotly.graph_objects as go
import Basic_Table as bt
import test_sandkey
import sandkey as sk
from Basic_Table import create_table

pn.extension("plotly")

# Print the columns to verify what is available
print(test_sandkey.df.columns)

# Define category filter widgets
table_category_filter = pn.widgets.Select(name='Table Category',
                                          options=list(test_sandkey.df['FuelCategoryRollup'].unique()))
sankey_category_filter = pn.widgets.Select(name='Sankey Category',
                                           options=list(test_sandkey.df['FuelCategoryRollup'].unique()))

# Define sliders to control Sankey node width and padding
node_width_slider = pn.widgets.IntSlider(name='Sankey Node Width', start=10, end=100, value=50)
node_pad_slider = pn.widgets.IntSlider(name='Sankey Node Padding', start=10, end=100, value=50)


# Callback function to update table and Sankey diagram based on filter
@pn.depends(table_category_filter.param.value, sankey_category_filter.param.value, node_width_slider.param.value,
            node_pad_slider.param.value)
def update_dashboard(table_category, sankey_category, node_width, node_pad):
    # Filter data for the table
    filtered_table_data = test_sandkey.df[test_sandkey.df['FuelCategoryRollup'] == table_category]

    # Filter data for the Sankey diagram
    filtered_sankey_data = test_sandkey.df[test_sandkey.df['FuelCategoryRollup'] == sankey_category]

    # Create table figure
    table_fig = create_table(filtered_table_data)

    # Create Sankey figure with user-controlled width and padding
    sankey_fig = sk.make_sankey(filtered_sankey_data, columns=['FuelCategoryRollup', 'FuelCategory'], vals_col='GenMw',
                                thickness=node_width, pad=node_pad)

    # Return the table and Sankey diagram in a Column layout
    return pn.Column(pn.panel(table_fig), pn.panel(sankey_fig))


# Create a layout for the dashboard
dashboard = pn.Column(
    pn.Row("### Interactive Dashboard with Plotly"),
    pn.Row(table_category_filter, sankey_category_filter),
    pn.Row(node_width_slider, node_pad_slider),
    pn.Row(pn.panel(update_dashboard, sizing_mode='stretch_width'))
)

# Serve the dashboard in the browser
pn.serve(dashboard)
