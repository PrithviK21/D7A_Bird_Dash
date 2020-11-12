import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from app import app
import urlgraph
import urlmap
import urlabout
import urldata

li = 'Welcome to our app! We have built an app that shows you the population distribution and records of 7 ' \
     'bird species. We have compiled our data from various sources around the internet including twitter.' \
     ' We have spared no effort in building this app. Our goal with this app is to help researchers and bird ' \
     'enthusiasts to easily access records and maps based on bird sighting data in the great state of Maharashtra.' \
     'We have tried to build this app with a user-friendly interface.'

howto = ['Each page allows you to filter based on bird species.',html.Br(),
         'On the Map page, there is an interactive map,'
         ' with hover data. On hovering, an image of the selected bird will be displayed.', html.Br(),
         'You can modify the time-frame for which the maps and graphs are generated.', html.Br(),
         'On the Graph page, we’ve included an adjustable graph and a  pie chart to help better understand the '
         'content. '
         'The adjustable graph can be a bar or a line graph using a dropdown list.', html.Br(), 'The Dataset page '
         'displays a filterable '
         'dataset which can also be sorted by any column.', html.Br(), 'The About page has info about us and the project.',
         html.Br(),'Have fun! ']

layout = html.Div(
    [
        html.Header([
            html.Div([
                html.Div([html.A('Bird Name', href='/Welcome')], className='logo'),
                html.Nav([
                    html.A('Map', href='/Map'),
                    html.A('Graphs', href='/Graph'),
                    html.A('Dataset', href='/Data'),
                    html.A('About', href='/About')
                ])
            ], className='wrapper')
        ]),
        html.Div([html.H2("Welcome to our app!")], className="banner"),
        html.Div([
            html.Div([
                html.H2("Introduction"),
                html.P(li),
                html.Hr(),
                html.H2("How to use:"),
                html.P(howto)
            ], className="content"),
        ], className='wrapper'),

        html.Footer(
            ['© CMPN SE Group 6 2020'],
            className='footer',
        )
    ], style={'background-color': '#449bb3', 'height': '1300px'}
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
], style={'background-color': '#449bb3', 'height': '1300px'})


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/Welcome' or pathname == '/':
        return layout
    if pathname == '/Graph':
        return urlgraph.layout
    elif pathname == '/Data':
        return urldata.layout
    elif pathname == '/Map':
        return urlmap.layout
    elif pathname == '/Graph':
        return urlgraph.layout
    elif pathname == '/About':
        return urlabout.layout


if __name__ == '__main__':
    app.run_server(debug=True)
