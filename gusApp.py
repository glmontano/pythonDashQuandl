import dash
import dash_core_components as dcc
import dash_html_components as html
import geopandas as gpd
from dash.dependencies import Input, Output

import quandl
import pandas as pd
import plotly.express as px

quandl.ApiConfig.api_key = "zGyHeGj9fVzHDHqLdBrU"
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

dataPathLoc = r"2021_data/gusActivityLocation.csv"
dataPathSup = r"2021_data/supportData.csv"
dataPathAct = r"2021_data/gusActivity.csv"

dfLoc = pd.read_csv(dataPathLoc, ",")
dfSup = pd.read_csv(dataPathSup, ",")
dfAct = pd.read_csv(dataPathAct, ",")

figLoc = px.scatter_geo(data_frame=dfLoc,
                     size="Count",
                     lat="Lat",
                     lon="Long",
                     color="City",
                     hover_name="City")

figSup = px.bar(dfSup, x='Name', y='Total')

figAct = px.line(dfAct, x="Date", y=["Daily Average", "Average Year"])#, color='country')


app.layout = html.Div(

    children=[

        html.H1(children='Gus using Python for Appraisal'),

        html.Div(children="Support activity"),
        html.Br(),
        dcc.Graph(id='support-graph', figure=figSup, style={'width': '175vh', 'height': '90vh'}),

        html.Div(children="Individual activity"),
        html.Br(),
        dcc.Graph(id='indiv-graph', figure=figAct, style={'width': '175vh', 'height': '90vh'}),

        html.Div(children="Location activity"),
        html.Br(),
        dcc.Graph(id='loc-graph', figure=figLoc, style={'width': '175vh', 'height': '90vh'}),

    ]
)

if __name__ == '__main__':
   app.run_server(host="0.0.0.0",debug=True)
