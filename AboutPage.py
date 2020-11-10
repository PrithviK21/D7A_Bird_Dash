import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(
    [
        html.Header([
            html.Div([
                html.Div([html.A('Bird Name', href='#')], className='logo'),
                html.Nav([
                    html.A('Map', href='#'),
                    html.A('Graphs', href='#'),
                    html.A('Dataset', href='#'),
                    html.A('About', href='#'),
                ])
            ], className='wrapper')
        ]),
        html.Div([html.H2("About Us")], className="banner"),
        html.Div([
            html.Div([
                html.H2("What is this app?"),
                html.P("App big good read map see bird"),
                html.H2("Who are we?"),
                html.P("Big stressy bois kaam bohot diya humko")], className="content"),
            ], className='wrapper'),

        html.Footer(
            ['Copyright my foot'],
            className='footer',
        )
    ], style={'background-color': '#449bb3', 'height': '1100px'}
)

if __name__ == '__main__':
    app.run_server(debug=True)
