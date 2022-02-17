import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import html
from dash import dcc
import plotly.express as px
import plotly.io as pio

pio.templates.default = 'plotly_dark'
df = pd.read_pickle('pic')
df.set_index('ID', inplace=True)
df.loc['Total'] = pd.Series(df.sum())
cols = df.columns
fig = px.line_polar(theta=cols, r=df.loc['Total'], line_close=True)
fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)')



app = dash.Dash( __name__, external_stylesheets=[dbc.themes.DARKLY])
card = {}
for col in cols:
    card[col] = dbc.Card([
        dbc.CardHeader(col),
        dbc.CardBody(
            html.H5(df.loc['Total',col], className="card-title"),
            ),
        ]
        ),


app.layout = html.Div([
    dbc.Row(
        dbc.Col(html.H1("Academic Dashboard",), width={"size": 12, 'offset':1},)
    ),
    html.Hr(),
    dbc.Row([
        dbc.Col(card['To Do'],),
        dbc.Col(card['Doing'],),
        dbc.Col(card['Done'],),
        dbc.Col(card['Non-Linear Structures'],),

    ],
    className="mb-4",),
    dbc.Row([
        dbc.Col(dbc.Card(dcc.Graph(figure=fig,), ),  width={"size": 6},),
        dbc.Col([
            dbc.Row([
                dbc.Col(card['Solar'],),
                dbc.Col(card['Advanced Composites'],),
            ],className="mb-4",),
            dbc.Row([
                dbc.Col(card['PfRP'],),
                dbc.Col(card['AVDASI4'],),
            ],className="mb-4",),
        ])
    ],className="mb-4",)
    ],
    )






if __name__ == "__main__":
    app.run_server(debug=True)

