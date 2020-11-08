import pandas as pd
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
#setting access token
token = 'pk.eyJ1IjoicHJpdGh2aWsyMSIsImEiOiJja2g0eHBpamkwYXB5MnNrMDNjaXFvNnRhIn0.6eeLvU-4xuLb8q43RAQGBA'
px.set_mapbox_access_token(token)
global df
df = pd.read_csv("finalMergedBirds/final_birds_fixed_dates.csv")
picdf = df[['Common_Name', 'mediaDownloadUrl']].copy()
picdf = picdf[picdf['mediaDownloadUrl'] != 'https://cdn.download.ams.birds.cornell.edu/api/v1/asset/']
#df = df[df['mediaDownloadUrl'] != 'https://cdn.download.ams.birds.cornell.edu/api/v1/asset/']
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
)
fig.update_layout(mapbox_style='dark',paper_bgcolor='#96dcd4')
fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
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
                    html.A('About', href='#'),
                ])
            ], className='wrapper')
        ]),
        html.Div(className='graphwindow', children=[dcc.Graph(id='mapboi', figure=fig)]),
        html.Div([html.Img(src='/assets/flam2.jpg',className='birdimg', id='birdimg')], className='frame'),
        html.Footer(
            ['Copyright my foot'],
            className='footer',
        )
    ], style={'background-color': '#449bb3', 'height': '100vh'}
)


@app.callback(Output('birdimg', 'src'),[Input('mapboi', 'hoverData')])
def return_birdimg(hover_data):
    m = hover_data['points'][0]['customdata'][2]
    name = hover_data['points'][0]['customdata'][0]
    bruh = picdf[picdf['Common_Name'] == name].sample().iloc[0]['mediaDownloadUrl']
    if m == 'https://cdn.download.ams.birds.cornell.edu/api/v1/asset/':
        return bruh
    return m


if __name__ == '__main__':
    app.run_server(debug=True)
