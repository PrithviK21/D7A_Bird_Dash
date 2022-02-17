import dash
from dash import dcc
from dash import html
import os
# from app import app

app = dash.Dash(__name__, suppress_callback_exceptions=True, update_title="Loading...", title="Pakshirashtra")
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])
import urlgraph
import urlmap
import urlabout
import urldata
import home

@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/Welcome' or pathname == '/':
        return home.layout
    # if pathname == '/Graph':
    #     return urlgraph.layout
    elif pathname == '/Data':
        return urldata.layout
    elif pathname == '/Map':
        return urlmap.layout
    elif pathname == '/Graph':
        return urlgraph.layout
    elif pathname == '/About':
        return urlabout.layout
    else:
        return html.Div([html.H1("ERROR 404: Page not found")])


if __name__ == '__main__':
    app.run_server(debug=False)
