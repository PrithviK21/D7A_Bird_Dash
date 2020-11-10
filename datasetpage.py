import pandas as pd
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_table
from datetime import date

global df
global dict_names

df = pd.read_csv("finalMergedBirds/final_birds_fixed_dates.csv")
df = df.drop(columns='mediaDownloadUrl')
df['Date'] = pd.to_datetime(df['Date'])
app = dash.Dash(__name__)
server = app.server

def create_dict_list_of_product():
    dictlist = []
    unique_list = df.Common_Name.unique()
    for product_title in unique_list:
        dictlist.append({'value': product_title, 'label': product_title})
    return dictlist


dict_names = create_dict_list_of_product()

app.layout = html.Div([
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
    html.Div([
        html.Div([
            html.H2('Choose a Bird'),
            dcc.Dropdown(
                id='product-dropdown',
                options=dict_names,
                value='Common Myna',
                multi=True
            ),
        ], className='dropdownFrame',style={'width': '40%', 'display': 'block'}),
        html.Div([
            html.H2("OG DATASET"),
            dash_table.DataTable(
                id='my-table',
                columns=[{"name": i, "id": i} for i in df.columns],
                style_cell={
                    'textAlign': 'left',
                    'overflow': 'hidden',
                    'textOverflow': 'ellipsis',
                    'maxWidth': 0,
                },
                tooltip_data=[
                    {
                        column: {'value': str(value), 'type': 'markdown'}
                        for column, value in row.items()
                    } for row in df.to_dict('rows')
                ],
                tooltip_duration=None
            )
        ],className='datasetFrame', style={'width': '100%', 'display': 'block'})
    ], style={'top': '110px', 'position': 'relative'}),
    html.Div(className='CalendarFrame', children=[
            dcc.DatePickerRange(min_date_allowed=date(2015, 1, 1),
                                max_date_allowed=date(2020, 10, 25),
                                initial_visible_month=date(2020, 10, 25),
                                start_date=date(2015, 1, 1),
                                end_date=date(2020, 10, 25),
                                display_format='Do/MMM/YYYY',
                                id="Date_Range")
        ], style={'top': '110px', 'right': '3%', 'position': 'absolute', 'display': 'inline-block'}),
], style={'background-color': '#449bb3', 'min-height': '1000px', 'height': 'auto'})

@app.callback(Output('my-table', 'data'), [Input('Date_Range', 'start_date'), Input('Date_Range', 'end_date'), Input('product-dropdown', 'value')])
def generate_table(start_date, end_date, selected_dropdown_value = None, max_rows=20):
    if len(selected_dropdown_value) == 0:
        datedf = df[(df['Date'] < end_date) & (df['Date'] > start_date)]
    else:
        if type(selected_dropdown_value) is str:
            filt_df = df[df['Common_Name'] == selected_dropdown_value]
        else:
            filt_df = df[(df['Common_Name'].isin(selected_dropdown_value))]
        datedf = filt_df[(filt_df['Date'] < end_date) & (filt_df['Date'] > start_date)]
    print(selected_dropdown_value)
    data = datedf.to_dict('records')
    return data

if __name__ == '__main__':
    app.run_server(debug=True)