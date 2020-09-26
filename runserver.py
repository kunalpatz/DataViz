"""
        *Data Visualization*
DASH: A simple data visualization tool

* DataSet Used:
    Malware dataset

* Authors:
    PATIL Kunal (Artificial Intelligence Systems)
    MARATH-PONMADOM (Data Science and Analytics)

"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
file = "Malware dataset.csv"
data = pd.read_csv(file)

fig = px.scatter(data, x="state", y="millisecond", size="millisecond",
                 color="hash", hover_name="classification")

app.layout = html.Div(children=[
    html.H1(children='Welcome to Sample Project using Dash'),
    html.H2(children='Created by Salil MARATH-PONMADOM and Kunal PATIL'),
    html.Div(children='''
        Malware Detection 
    '''),
    dcc.Graph(
        id='malware1',
        figure=fig
    )
])
if __name__ == '__main__':
    app.run_server(debug=True)