from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as plt
import pandas as pd

df= pd.read_csv(r"C:\Users\rahul\OneDrive\Desktop\Forage\Quantium_\Jupyter\output_data.csv")

app = Dash(__name__)



app.layout = html.Div(children=[
    html.H1(children='Sales of soul food over different dates'),
    dcc.RadioItems(options=[
       {'label': 'North', 'value': 'north'},
        {'label': 'East', 'value': 'east'},
        {'label': 'South', 'value': 'south'},
        {'label': 'West', 'value': 'west'},
        {'label': 'All', 'value': 'all'}
    ],value='all',id='region',inline=True),
    dcc.Graph(id='line-chart')
])

@callback(
    Output('line-chart','figure'),
    Input('region','value')
)
def update_region(region_value):
    if region_value == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region']==region_value]

    fig = plt.line(filtered_df,x='date',y='sales')
    return fig

if __name__ =='__main__':
    app.run(debug=True)