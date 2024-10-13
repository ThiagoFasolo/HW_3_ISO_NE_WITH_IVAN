import plotly.graph_objects as go




def create_table(data):
    # Creates table using the data
    figure = go.Figure(data=[go.Table(
        # Builds and Styles the first row (titles) of the table
        header=dict(values=list(data.columns),
                    fill_color="grey",
                    align = 'left'),
        cells = dict(values=[data[columns] for columns in data.columns],
                     fill_color="lightgrey",
                     align='left'))
    ])
    figure.show()

create_table()