import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import quandl
import pandas as pd
import plotly.express as px

quandl.ApiConfig.api_key = "zGyHeGj9fVzHDHqLdBrU"
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# CHRIS/CME_NN1 - Henry Hub
# CHRIS/CME_CL1 - Crude Oil
# CHRIS/ICE_SB4 - Sugar Futures

hhData = quandl.get("CHRIS/CME_NN1", returns="numpy")
hhDates = hhData["Date"]
hhPrices = hhData["Settle"]
hhDf = pd.DataFrame({"Dates": hhDates, "Prices": hhPrices})

coData = quandl.get("CHRIS/CME_CL1", returns="numpy")
coDates = coData["Date"]
coPrices = coData["Settle"]
coDf = pd.DataFrame({"Dates": coDates, "Prices": coPrices})

sgData = quandl.get("CHRIS/ICE_SB1", returns="numpy")
sgDates = sgData["Date"]
sgPrices = sgData["Settle"]
sgDf = pd.DataFrame({"Dates": sgDates, "Prices": sgPrices})

hhFig = px.line(data_frame=hhDf, x="Dates", y="Prices")
coFig = px.line(data_frame=coDf, x="Dates", y="Prices")
sgFig = px.line(data_frame=sgDf, x="Dates", y="Prices")

app.layout = html.Div(

    children=[

        html.H1(children='Gus quickly working with PlotyExpress and Dash!'),
        html.Div(children="Navigate between API Henry Hub and Crude Oil data; Zoom in & Explore!."),
        html.Br(),
        html.Button("Henry Hub", id="btn-henryHub", n_clicks=0),
        html.Button("Crude Oil", id="btn-crudeOil", n_clicks=0),
        html.Button("Sugar Futures", id="btn-sugar", n_clicks=0),
        dcc.Graph(id='the-graph', figure=hhFig)
    ]
)

# Whenever and input is changed - this section of the code is called back, and I believe
# the code beneath it also activated
@app.callback(
    Output("the-graph", "figure"),
    [Input("btn-henryHub", "n_clicks"),
    Input("btn-crudeOil", "n_clicks"),
    Input("btn-sugar", "n_clicks")])

def updateGraph(btn1, btn2, btn3):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if "btn-henryHub" in changed_id:
        figOut = hhFig
    elif "btn-crudeOil" in changed_id:
        figOut = coFig
    elif "btn-sugar" in changed_id:
        figOut = sgFig
    else:
        figOut = hhFig
    return figOut

if __name__ == '__main__':
   app.run_server(host="0.0.0.0",debug=True)
