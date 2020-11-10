import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
li = 'Welcome to our app!. We have built an app that shows you the population distribution and records of 7 bird species.' \
     ' We have compiled our data from various sources around the internet including twitter.' \
     ' We have spared no effort in building this app. Our goal with this app is to help researchers and bird enthusiasts' \
     ' to easily access records and maps based on bird sighting data in the great state of Maharashtra.We have tried to build' \
     ' this app with a user-friendly interface..'
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
        html.Div([html.H2("Welcome to our app!")], className="banner"),
        html.Div([
            html.Div([
                html.H2("Content goes here"),
                html.P(li)], className="content"),
            ], className='wrapper'),

        html.Footer(
            ['Copyright my foot'],
            className='footer',
        )
    ], style={'background-color': '#449bb3', 'height': '1300px'}
)

if __name__ == '__main__':
    app.run_server(debug=True)
