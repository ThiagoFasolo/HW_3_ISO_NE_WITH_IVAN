import panel as pn
import datetime

# Define the exclude energy source widget
exclude_energy_source_widget = pn.widgets.CheckBoxGroup(
    name='Exclude Energy Source',
    value=[],
    options=['Solar', 'Wind', 'Hydro', 'Natural Gas', 'Nuclear', 'Landfill Gas', 'Refuse', 'Wood', 'Oil', 'Other']
    )

# Date range widget for selecting a date range
date_range_widget = pn.widgets.DateRangePicker(
    name="Select Date Range",
    start=datetime.date(2024, 8, 1),  # Start date
    end=datetime.date.today(),  # Today's date
    value=(datetime.date.today(), datetime.date.today())  # Default range
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