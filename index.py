import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import client


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return client.layout
    elif pathname == '/apps/client':
        return client.layout
    else:
        return '404 Page Not Found!'


if __name__ == '__main__':
    app.run_server(debug=True)
