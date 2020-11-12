import pandas as pd
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from datetime import date

# setting access token
token = 'pk.eyJ1IjoicHJpdGh2aWsyMSIsImEiOiJja2g0eHBpamkwYXB5MnNrMDNjaXFvNnRhIn0.6eeLvU-4xuLb8q43RAQGBA'
px.set_mapbox_access_token(token)
global df
df = pd.read_csv("finalMergedBirds/final_birds_fixed_dates.csv")
df['Date'] = pd.to_datetime(df['Date'])

picdf = df[['Common_Name', 'mediaDownloadUrl']].copy()
picdf = picdf[picdf['mediaDownloadUrl'] != 'https://cdn.download.ams.birds.cornell.edu/api/v1/asset/']
# df = df[df['mediaDownloadUrl'] != 'https://cdn.download.ams.birds.cornell.edu/api/v1/asset/']

app = dash.Dash(__name__)
server = app.server
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
fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))

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
        html.Div(className='graphwindow', children=[dcc.Graph(id='mapboi', figure=fig, responsive=True)]),
        html.Div([
            dcc.DatePickerRange(min_date_allowed=date(2015, 1, 1),
                                max_date_allowed=date(2020, 10, 25),
                                initial_visible_month=date(2020, 10, 25),
                                start_date=date(2015, 1, 1),
                                end_date=date(2020, 10, 25),
                                display_format='Do/MMM/YYYY',
                                id="Date_Range")
        ], style={'top': '18%', 'left': '3%', 'position': 'absolute'}),
        html.Div([html.H2(id='birdtitle'),html.Img(src='/assets/flam2.jpg', className='birdimg', id='birdimg')], className='frame'),
        html.Footer(
            ['© CMPN SE Group 6 2020'],
            className='footer',
        )
    ], style={'background-color': '#449bb3', 'height': '100vh'}
)


@app.callback(Output('birdimg', 'src'),Output('birdtitle', 'children'), [Input('mapboi', 'hoverData')])
def return_birdimg(hover_data):
    if hover_data is not None:
        m = hover_data['points'][0]['customdata'][2]
        name = hover_data['points'][0]['customdata'][0]
        bruh = picdf[picdf['Common_Name'] == name].sample().iloc[0]['mediaDownloadUrl']
        if m == 'https://cdn.download.ams.birds.cornell.edu/api/v1/asset/':
            return [bruh, name]
        return [m, name]
    else:
        return ['assets/flam2.jpg', 'Common Name']


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
    )
    fig.update_layout(mapbox_style='dark', paper_bgcolor='#96dcd4')
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
