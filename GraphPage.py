import pandas as pd
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_table

global df
global dict_names

df = pd.read_csv("finalMergedBirds/final_birds_fixed_dates.csv")
app = dash.Dash(__name__)
server = app.server

def create_dict_list_of_product():
    dictlist = []
    unique_list = df.Common_Name.unique()
    for product_title in unique_list:
        dictlist.append({'value': product_title, 'label': product_title})
    return dictlist


dict_names = create_dict_list_of_product()

stuff = dict()
for name in df['Common_Name']:
    stuff[name] = df['Common_Name'].value_counts()[name]
sdf = pd.DataFrame({
    'Common_Name': stuff.keys(),
    'Count': stuff.values()}
)
piec = px.pie(sdf, values = 'Count', names = 'Common_Name')

app.layout = html.Div([
        html.Div([
            html.H1('Birds be wildin'),
            html.H2('Choose a Bird'),
            dcc.Dropdown(
                id='product-dropdown',
                options=dict_names,
                value='Common Myna'
            ),
            dcc.Dropdown(
                id='graph-type',
                options=[{'value': 'BAR', 'label': 'Bar'},
                         {'value': 'LINE', 'label': 'Line'}],
                value='BAR'),
            dcc.Graph(id = 'graphs')
        ], style={'width': '40%', 'display': 'inline-block'}),

        html.Div([
            html.H1("Pie Chart"),
            dcc.Graph(
                id='pie',
                figure=piec
            )
        ], style={'width': '40%', 'display': 'inline-block'}),
        # html.Div([
        #     html.H2("OG DATASET"),
        #     dash_table.DataTable(
        #         id='my-table',
        #         columns=[{"name": i, "id": i} for i in df.columns],
        #         style_cell={
        #             'textAlign': 'left',
        #             'overflow': 'hidden',
        #             'textOverflow': 'ellipsis',
        #             'maxWidth': 0,
        #         },
        #         tooltip_data=[
        #             {
        #                 column: {'value': str(value), 'type': 'markdown'}
        #                 for column, value in row.items()
        #             } for row in df.to_dict('rows')
        #         ],
        #         tooltip_duration=None
        #         )
        # ])
])


# @app.callback(Output('my-table', 'data'), [Input('product-dropdown', 'value')])
# def generate_table(selected_dropdown_value=None, max_rows=20):
#     filt_df = df.loc[df['Common_Name'] == selected_dropdown_value]
#     data = df.to_dict('records')
#     return data

@app.callback(Output('graphs', 'figure'), [Input('product-dropdown', 'value'), Input('graph-type', 'value')])
def generate_graph(dropdown_value, graph_type):
    xdf = df.loc[df['Common_Name'] == dropdown_value]
    if graph_type == 'BAR':
        fig = px.bar(xdf, x=xdf.Date, y=xdf.index, title='bar graph')
    elif graph_type == 'LINE':
        fig = px.line(xdf, y=xdf.Date, x=xdf.index, title='line graph')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)