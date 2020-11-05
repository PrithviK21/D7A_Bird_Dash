import pandas as pd
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import chart_studio as cs

# setting user, api key and access token
#cs.tools.set_credentials_file(username='PrithviK21', api_key='tyPPENMPBtDHJK9TMTxH')
token = 'pk.eyJ1IjoicHJpdGh2aWsyMSIsImEiOiJja2g0eHBpamkwYXB5MnNrMDNjaXFvNnRhIn0.6eeLvU-4xuLb8q43RAQGBA'
px.set_mapbox_access_token(token)
global df
df = pd.read_csv("finalMergedBirds/final_birds_fixed_dates.csv")
#df = df.loc[df['Common_Name'] == 'Greater Flamingo']
df['Date'] = df['Date'].apply(lambda x:  (int)(x.split('/')[2]))
df = df.sort_values('Date',ascending=True)
fig = px.scatter_mapbox(
    df,
    lat=df['Latitude'],
    lon=df['Longitude'],
    color='Common_Name',
    animation_frame="Date",
    animation_group='Common_Name',
    width=800,
    height=600
    )
fig.update_layout(mapbox_style='dark')
fig.update_layout(margin=dict(t=0,b=0,l=0,r=0))
# layout = dict(
#     height=800,
#     # top, bottom, left and right margins
#     margin=dict(t=0, b=0, l=0, r=0),
#     font=dict(color='#FFFFFF', size=11),
#     paper_bgcolor='#000000',
#     mapbox=dict(
#         # here you need the token from Mapbox
#         accesstoken=mapbox_access_token,
#         bearing=0,
#         # where we want the map to be centered
#         center=dict(
#             lat=18,
#             lon=72
#         ),
#         # we want the map to be "parallel" to our screen, with no angle
#         pitch=0,
#         # default level of zoom
#         zoom=3,
#         # default map style
#         style='dark'
#     )
# )


app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    dcc.Graph(id='mapboi', figure=fig),
])

if __name__ == '__main__':
    app.run_server(debug=True)