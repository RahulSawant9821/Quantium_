from dash import Dash,html,dcc
import plotly.express as plt
import pandas as pd

df= pd.read_csv(r"C:\Users\rahul\OneDrive\Desktop\Forage\Quantium_\Jupyter\output_data.csv")

app = Dash(__name__)

fig = plt.line(df,x='date',y='sales',color='region')

app.layout = html.Div(children=[
    html.H1(children='Sales of soul food over different dates'),

    dcc.Graph(id='line-chart',figure=fig)
])

if __name__ =='__main__':
    app.run(debug=True)