import panel as pn
import pandas as pd
import plotly.graph_objects as go
import Basic_Table as bt

pn.extension("plotly")

category_filter = pn.widgets.Select(name = 'Category',
                                    options = list(data['category'].unique()))

def update_table(cater)