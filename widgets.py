import panel as pn
import datetime

# Define the energy source widget
energy_source_widget = pn.widgets.Select(
    name="Energy Source",
    options=['Solar', 'Wind', 'Hydro', 'Natural Gas'],
    value='Solar'
)

# Date range widget for selecting a date range
date_range_widget = pn.widgets.DateRangePicker(
    name="Select Date Range",
    start=datetime.date(2024, 9, 1),  # Start date
    end=datetime.date.today(),  # Today's date
    value=(datetime.date(2024, 9, 1), datetime.date.today(),)  # Default range
)

# Plot size adjustment sliders
width_slider = pn.widgets.IntSlider(name="Plot Width", start=300, end=2000, step=100, value=1200)
height_slider = pn.widgets.IntSlider(name="Plot Height", start=300, end=1500, step=100, value=800)


# New widget to select the category type for the line graph and Sankey diagram
category_type_widget = pn.widgets.Select(
    name="Category Type",
    options=['FuelCategory', 'FuelCategoryRollup'],  # Options to toggle between different fuel categories
    value='FuelCategory'  # Default to 'FuelCategory'
)