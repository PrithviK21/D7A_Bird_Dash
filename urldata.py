import pandas as pd
from dash.dependencies import Input, Output
from dash import dcc
from dash import html
from dash import dash_table
from dash import callback
from datetime import date
# from mainAppPage import app

global df
global dict_names

df = pd.read_csv("finalMergedBirds/finalbirdsSEM4.csv")
df = df.drop(columns='mediaDownloadUrl')
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')


def create_dict_list_of_product():
    dictlist = []
    unique_list = df.Common_Name.unique()
    for product_title in unique_list:
        dictlist.append({'value': product_title, 'label': product_title})
    return dictlist


dict_names = create_dict_list_of_product()

layout = html.Div([
    html.Div([html.Header([
        html.Div([
            html.Div([html.A('Pakshirashtra', href='/Welcome')], className='logo'),
            html.Nav([
                html.A('Map', href='/Map'),
                html.A('Graphs', href='/Graph'),
                html.A('Dataset', href='/Data'),
                html.A('About', href='/About')
            ])
        ], className='wrapper')
    ], className='normal-header')]),
    html.Div([
        html.H1("Dataset"),
        html.Div([html.Div([
            dcc.Dropdown(
                id='product-dropdown',
                options=dict_names,
                multi=True
            ),
        ], className='dropdownFrame'),
        html.Div([
        dcc.DatePickerRange(min_date_allowed=date(2015, 1, 1),
                            max_date_allowed=date(2020, 10, 25),
                            initial_visible_month=date(2020, 10, 25),
                            start_date=date(2015, 1, 1),
                            end_date=date(2020, 10, 25),
                            display_format='Do/MMM/YYYY',
                            id="Date_Range")
    ])], className='filter-container'),
        html.Div([
            dash_table.DataTable(
                id='my-table',
                columns=[{"name": i, "id": i} for i in df.columns],
                sort_action='native',
                page_size=30,
                style_table={'height': '490px', 'overflowY': 'auto'},
                style_cell={
                    'textAlign': 'left',
                    'overflow': 'hidden',
                    'textOverflow': 'ellipsis',
                    'maxWidth': 0,
                },
                style_cell_conditional=[
                    {
                        'if': {'column_id': c},
                        'textAlign': 'left'
                    } for c in ['Date', 'Region']
                ],
                style_data_conditional=[
                    {
                        'if': {'row_index': 'odd'},
                        'backgroundColor': 'rgb(248, 248, 248)'
                    }
                ],
                style_header={
                    'backgroundColor': 'rgb(230, 230, 230)',
                    'fontWeight': 'bold',
                    'border': '2px solid black'
                },
            )
        ], className='DatasetFrame')
    ], className='containerdiv'),
    
   
])


@callback(Output('my-table', 'data'),
              [Input('Date_Range', 'start_date'), Input('Date_Range', 'end_date'), Input('product-dropdown', 'value')])
def generate_table(start_date, end_date, selected_dropdown_value=None, max_rows=20):
    if (selected_dropdown_value is None) or (len(selected_dropdown_value) == 0):
        datedf = df[(df['Date'] < end_date) & (df['Date'] > start_date)]
    else:
        if type(selected_dropdown_value) is str:
            filt_df = df[df['Common_Name'] == selected_dropdown_value]
        else:
            filt_df = df[(df['Common_Name'].isin(selected_dropdown_value))]
        datedf = filt_df[(filt_df['Date'] < end_date) & (filt_df['Date'] > start_date)]
    data = datedf.to_dict('records')
    return data
