# import dash_core_components as dcc
import dash_html_components as html
# from dash.dependencies import Input, Output
# from app import app
import requests, json

# call the API
api_url = "http://localhost:9000/api"
data = json.dumps({'sl': 5.84, 'sw': 3.0, 'pl': 3.75, 'pw': 1.1})
r = requests.post(api_url, data)
r = str(r.json())

# Display the result
layout = html.Div(children=[
    html.H1(children=r)
])