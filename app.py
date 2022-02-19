import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import html, dash_table
from dash import dcc
import plotly.express as px
import plotly.io as pio
import trelloAPI as tr
import seecrets

pio.templates.default = 'plotly_dark'
df = pd.read_pickle('pic')
df.set_index('ID', inplace=True)
dic = df['Wind'].value_counts()
#cols = df.columns
fig = px.line_polar(theta=dic.index, r=dic, line_close=True)
fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)')
app = dash.Dash( __name__, external_stylesheets=[dbc.themes.DARKLY])



app.layout = html.Div([
    dbc.Row(
        dbc.Col(html.H1("Daisy's Weather Dashboard",), width={"size": 12, 'offset':1},)
    ),
    html.Hr(),
    dbc.Row([


    ],
    className="mb-4",),
    dbc.Row([
        dbc.Col(dbc.Card(dcc.Graph(figure=fig,), ),  width={"size": 6},),
        dbc.Col([
            dbc.Row([

            ],className="mb-4",),
            dbc.Row([

            ],className="mb-4",),
        ])
    ],className="mb-4",)
    ],
    )






if __name__ == "__main__":
    app.run_server(debug=True)

