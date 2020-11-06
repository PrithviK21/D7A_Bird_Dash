import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# setting access token
token = 'pk.eyJ1IjoicHJpdGh2aWsyMSIsImEiOiJja2g0eHBpamkwYXB5MnNrMDNjaXFvNnRhIn0.6eeLvU-4xuLb8q43RAQGBA'
px.set_mapbox_access_token(token)
global df
df = pd.read_csv("finalMergedBirds/final_birds_fixed_dates.csv")
# df = df.loc[df['Common_Name'] == 'Greater Flamingo']
df['Date'] = df['Date'].apply(lambda x: int(x.split('/')[2]))
df = df.sort_values('Date', ascending=True)
fig = px.scatter_mapbox(
    df,
    lat=df['Latitude'],
    lon=df['Longitude'],
    color='Common_Name',
    width=800,
    height=600,
)
fig.update_layout(mapbox_style='dark', paper_bgcolor='#72aeb2')
fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(
    [
        html.Header([
            html.Div([
                html.Nav([
                    html.A('Map', href='#'),
                    html.A('Graphs', href='#'),
                    html.A('About', href='#'),
                ])
            ], className='wrapper')
        ]),
        html.Div(className='graph', children=[dcc.Graph(id='mapboi', figure=fig)], ),

        html.Footer(
            ['Copyright my foot'],
            className='footer',
        )

    ], style={'background-color': '#385d5f', 'position': 'relative', 'min-height': '100vh'}
)

if __name__ == '__main__':
    app.run_server(debug=True)
