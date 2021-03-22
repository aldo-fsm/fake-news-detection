from typing import Text
import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.CardHeader import CardHeader
import dash_html_components as html

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = dbc.Container(
    dbc.Col([
        dbc.Textarea(),
        dbc.Row(
            dbc.Card([
                dbc.CardHeader(
                    html.H1('oi', className='card-title'),
                ),
                dbc.CardBody('oi')
            ])
        ),
        dbc.Row('oi'),
    ])
    , className='mt-4')

if __name__ == "__main__":
    app.run_server(
        debug=True,
        dev_tools_hot_reload=True
    )