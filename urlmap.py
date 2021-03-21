import pandas as pd
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from datetime import date
from app import app
import clustering

# setting access token
token = 'pk.eyJ1IjoicHJpdGh2aWsyMSIsImEiOiJja2g0eHBpamkwYXB5MnNrMDNjaXFvNnRhIn0.6eeLvU-4xuLb8q43RAQGBA'
px.set_mapbox_access_token(token)
global df
global new_df
global dict_names
global new_dict_names

df = pd.read_csv("finalMergedBirds/birdsNewLinks.csv")
df['Date'] = pd.to_datetime(df['Date'])

new_df = clustering.clusterset(df)
new_df['Date'] = pd.to_datetime(df['Date'])

# picdf = df[['Common_Name', 'mediaDownloadUrl']].copy()
# picdf = picdf[picdf['mediaDownloadUrl'] != 'https://cdn.download.ams.birds.cornell.edu/api/v1/asset/']
# df = df[df['mediaDownloadUrl'] != 'https://cdn.download.ams.birds.cornell.edu/api/v1/asset/']
tab_style = {
    'borderTop': '1px solid #000000',
    'borderBottom': '1px solid #000000',
    'color': '#515151',
    'backgroundColor': '#96dcd4',
    'padding': '6px',
    'fontWeight': 'bold',
    'fontFamily': 'code',
}

tab_selected_style = {

    'backgroundColor': '#ffff',
    'fontWeight': 'bold',
    'fontFamily': 'code',
    'color': 'black',
    'padding': '6px'
}
fig = px.scatter_mapbox(
    df,
    lat=df['Latitude'],
    lon=df['Longitude'],
    color='Common_Name',
    hover_name='Common_Name',
    hover_data={'Common_Name': False, 'Date': True, 'mediaDownloadUrl': ':[0:0]'},
    width=800,
    height=600,
    opacity=0.7,
    zoom=4.5
)
fig.update_layout(mapbox_style='dark', paper_bgcolor='#96dcd4', title='bruh')
fig.update_layout(margin=dict(t=0, b=0, l=0, r=0), legend_title_text='Birds')

clusterfig = px.scatter_mapbox(
    new_df,
    lat=new_df['Latitude'],
    lon=new_df['Longitude'],
    color='Cluster',
    hover_name='Cluster',
    hover_data={'Cluster': False, 'Date': True, 'mediaDownloadUrl': ':[0:0]'},
    width=800,
    height=600,
    opacity=0.7,
    zoom=4.5
)
clusterfig.update_layout(mapbox_style='dark', paper_bgcolor='#96dcd4', title='bruh')
clusterfig.update_layout(margin=dict(t=0, b=0, l=0, r=0), legend_title_text='Regions')

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
        ]),

        html.Div([
            dcc.Tabs([
                dcc.Tab(label='Species',
                        style=tab_style, selected_style=tab_selected_style, children=[
                        html.Div([
                            html.Div([dcc.Graph(id='mapboi', figure=fig, responsive=True)],
                                     style={'top': '330%', 'left': '2.5%', 'width': '55%', 'display': 'block',
                                            'position': 'absolute'}),
                            html.Div([
                                dcc.DatePickerRange(min_date_allowed=date(2015, 1, 1),
                                                    max_date_allowed=date(2020, 10, 25),
                                                    initial_visible_month=date(2020, 10, 25),
                                                    start_date=date(2015, 1, 1),
                                                    end_date=date(2020, 10, 25),
                                                    display_format='Do/MMM/YYYY',
                                                    id="Date_Range")
                            ], style={'top': '120%', 'left': '3%', 'position': 'absolute'}),
                            html.Div([html.H2(id='birdtitle'),
                                      html.Img(src='/assets/flam2.jpg', className='birdimg', id='birdimg')],
                                     className='frame'),

                        ])

                    ]),
                dcc.Tab(label='Clusters', style=tab_style, selected_style=tab_selected_style, children=[
                    html.Div([
                        html.Div(children=[dcc.Graph(id='clustermapboi', figure=clusterfig, responsive=True)],
                                 style={'top': '330%', 'left': '2.5%', 'width': '55%', 'display': 'block',
                                        'position': 'absolute'}),
                        html.Div([
                            dcc.DatePickerRange(min_date_allowed=date(2015, 1, 1),
                                                max_date_allowed=date(2020, 10, 25),
                                                initial_visible_month=date(2020, 10, 25),
                                                start_date=date(2015, 1, 1),
                                                end_date=date(2020, 10, 25),
                                                display_format='Do/MMM/YYYY',
                                                id="clusterDate_Range")
                        ], style={'top': '120%', 'left': '3%', 'position': 'absolute'}),
                        html.Div([html.H2(id='clusterbirdtitle'),
                                  html.Img(src='/assets/flam2.jpg', className='clusterbirdimg', id='clusterbirdimg')],
                                 className='frame'),

                    ]),

                ])

            ])

        ], style={'top': '17%', 'left': '2.5%', 'width': '95%', 'display': 'block', 'position': 'absolute'}),

        html.Footer(
            ['© CMPN SE Group 6 2020-2021'],
            className='footer',
        )
    ], style={'background-color': '#449bb3', 'height': '100vh'}
)


@app.callback(Output('birdimg', 'src'), Output('birdtitle', 'children'), [Input('mapboi', 'hoverData')])
def return_birdimg(hover_data):
    if hover_data is not None:
        m = hover_data['points'][0]['customdata'][2]
        name = hover_data['points'][0]['customdata'][0]
        # bruh = picdf[picdf['Common_Name'] == name].sample().iloc[0]['mediaDownloadUrl']
        # if m == 'https://cdn.download.ams.birds.cornell.edu/api/v1/asset/':
        #     return [bruh, name]
        return [m, name]
    else:
        return ['assets/flam2.jpg', 'Common Name']


"""html.Div([
    dcc.Tabs([
        dcc.Tab(label='Tab One', children=[
            dcc.Graph(id='clustermapboi', figure=clusterfig, responsive=True)
            ]),
        dcc.Tab(label='Tab Two', children=[
            dcc.Graph(id='mapboi', figure=fig, responsive=True)
            ]),

    ]),
], className='graphwindow' ),
html.Div([
    dcc.DatePickerRange(min_date_allowed=date(2015, 1, 1),
                        max_date_allowed=date(2020, 10, 25),
                        initial_visible_month=date(2020, 10, 25),
                        start_date=date(2015, 1, 1),
                        end_date=date(2020, 10, 25),
                        display_format='Do/MMM/YYYY',
                        id="Date_Range")
], style={'top': '18%', 'left': '3%', 'position': 'absolute'}),
html.Div([html.H2(id='birdtitle'), html.Img(src='/assets/flam2.jpg', className='birdimg', id='birdimg')],
         className='frame'),"""


@app.callback(Output('clusterbirdimg', 'src'), Output('clusterbirdtitle', 'children'),
              [Input('clustermapboi', 'hoverData')])
def return_birdimg(hover_data):
    if hover_data is not None:
        m = hover_data['points'][0]['customdata'][2]
        name = hover_data['points'][0]['customdata'][0]
        # bruh = picdf[picdf['Common_Name'] == name].sample().iloc[0]['mediaDownloadUrl']
        # if m == 'https://cdn.download.ams.birds.cornell.edu/api/v1/asset/':
        #     return [bruh, name]
        return [m, name]
    else:
        return ['assets/flam2.jpg', 'Cluster']


@app.callback(Output('mapboi', 'figure'), [Input('Date_Range', 'start_date'), Input('Date_Range', 'end_date')])
def update_graph_date(start_date, end_date):
    datedf = df[(df['Date'] < end_date) & (df['Date'] > start_date)]
    fig = px.scatter_mapbox(
        datedf,
        lat=datedf['Latitude'],
        lon=datedf['Longitude'],
        color='Common_Name',
        hover_name='Common_Name',
        hover_data={'Common_Name': False, 'Date': True, 'mediaDownloadUrl': ':[0:0]'},
        width=800,
        height=600,
        opacity=0.7,
        zoom = 4.5
    )
    fig.update_layout(mapbox_style='dark', paper_bgcolor='#96dcd4')
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0), legend_title_text='Birds')
    return fig


@app.callback(Output('clustermapboi', 'figure'),
              [Input('clusterDate_Range', 'start_date'), Input('clusterDate_Range', 'end_date')])
def update_graph_date(start_date, end_date):
    datedf = new_df[(new_df['Date'] < end_date) & (new_df['Date'] > start_date)]
    clusterfig = px.scatter_mapbox(
        datedf,
        lat=datedf['Latitude'],
        lon=datedf['Longitude'],
        color='Cluster',
        hover_name='Cluster',
        hover_data={'Cluster': False, 'Date': True, 'mediaDownloadUrl': ':[0:0]'},
        width=800,
        height=600,
        opacity=0.7,
        zoom=4.5
    )
    clusterfig.update_layout(mapbox_style='dark', paper_bgcolor='#96dcd4')
    clusterfig.update_layout(margin=dict(t=0, b=0, l=0, r=0), legend_title_text='Regions')
    return clusterfig
