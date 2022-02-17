import dash
from dash import dcc
from dash import html

li = 'Welcome to our app! We have built an app that shows you the population distribution and records of 7 ' \
     'bird species. We have compiled our data from various sources around the internet including twitter.' \
     ' We have spared no effort in building this app. Our goal with this app is to help researchers and bird ' \
     'enthusiasts to easily access records and maps based on bird sighting data in the great state of Maharashtra.' \
     'We have tried to build this app with a user-friendly interface. Additionally, we have implemented Clustering, to ' \
     'help give an idea of the regions in which birds are found. This can be accessed on the map and graph page by ' \
     'clicking on the cluster tab.'

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
                html.Div([html.A('Pakshirashtra', href='/Welcome')], className='logo'),
                html.Nav([
                    html.A('Map', href='/Map'),
                    html.A('Graphs', href='/Graph'),
                    html.A('Dataset', href='/Data'),
                    html.A('About', href='/About')
                ])
            ], className='wrapper')
        ], className='home-header'),
        html.Div([html.H2("Welcome to our app!")], className="banner"),
        html.Div([
            html.Div([
                html.H2("Introduction"),
                html.P(li),
                html.Hr(),
                html.H2("How to use:"),
                html.P(howto)
            ], className="content"),
        ], className='banner-content'),

        html.Footer(
            ['© CMPN SE Group 6 2020-2021'],
            className='footer',
        )
    ], className='homepage'
)
