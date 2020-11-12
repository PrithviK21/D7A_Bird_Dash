import pandas as pd
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from datetime import date
import plotly.io as plt_io

global df
global dict_names

df = pd.read_csv("finalMergedBirds/final_birds_fixed_dates.csv")
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

plt_io.templates['custom'] = plt_io.templates['plotly_dark']
plt_io.templates['custom']['layout']['paper_bgcolor'] = '#96dcd4'
plt_io.templates['custom']['layout']['plot_bgcolor'] = '#96dcd4'
plt_io.templates['custom']['layout']['font']['color'] = '#000000'
plt_io.templates['custom']['layout']['font']['color'] = '#000000'

stuff = dict()
for name in df['Common_Name']:
    stuff[name] = df['Common_Name'].value_counts()[name]
sdf = pd.DataFrame({
    'Common_Name': stuff.keys(),
    'Count': stuff.values()}
)
piec = px.pie(sdf, values = 'Count', names = 'Common_Name', title='Pie Chart', template = 'custom')
piec.update_traces(marker=dict(line=dict(color='#000000', width=0.5)))
piec.update_layout(title={'y':0.9, 'x':0.5, 'xanchor': 'center'})

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
        dcc.Dropdown(
            id='graph-type',
            options=[{'value': 'BAR', 'label': 'Bar'},
                     {'value': 'LINE', 'label': 'Line'}],
            value='BAR'),
        dcc.Dropdown(
            id='product-dropdown',
            options=dict_names,
            multi=True,
            placeholder='Select Birds'
        )
    ], className='dropdownFrame', style={'top': '30%','width': '25%', 'left': '5%', 'position': 'absolute', 'display': 'block'}),
    html.Div([
        dcc.Graph(id = 'graphs')
    ], style={'box-shadow': '2px 2px 2px black', 'top': '42.5%', 'left': '2.5%','width': '45%', 'position': 'absolute','display': 'block'}),
    html.Div([html.H1("Pie Chart")], style={'top': '25%', 'left': '70%', 'position': 'absolute'}),
    html.Div([
        dcc.Graph(
            id='pie',
            figure=piec
        )
    ], style={'box-shadow': '2px 2px 2px black', 'top': '42.5%', 'left': '52.5%', 'width': '45%', 'position': 'absolute', 'display': 'block'}),
    html.Div(className='CalendarFrame', children=[
            dcc.DatePickerRange(min_date_allowed=date(2015, 1, 1),
                                max_date_allowed=date(2020, 10, 25),
                                initial_visible_month=date(2020, 10, 25),
                                start_date=date(2015, 1, 1),
                                end_date=date(2020, 10, 25),
                                display_format='Do/MMM/YYYY',
                                id="Date_Range")
    ], style={'top': '17%', 'left': '5%', 'position': 'absolute', 'display': 'block'})
], style={'background-color': '#449bb3', 'min-height': '1000px'})

@app.callback(Output('graphs', 'figure'), [Input('Date_Range', 'start_date'), Input('Date_Range', 'end_date'),Input('graph-type', 'value'), Input('product-dropdown', 'value')])
def generate_graph(start_date, end_date, graph_type, selected_dropdown_value = None):
    if (selected_dropdown_value is None) or (len(selected_dropdown_value) == 0):
        datedf = df[(df['Date'] < end_date) & (df['Date'] > start_date)].copy()
        cdf = sdf
        cdf = cdf.rename(columns={'Common_Name':'Bird'})
    else:
        if type(selected_dropdown_value) is str:
            xdf = df[df['Common_Name'] == selected_dropdown_value]
        else:
            xdf = df[(df['Common_Name'].isin(selected_dropdown_value))]
        datedf = xdf[(xdf['Date'] < end_date) & (xdf['Date'] > start_date)].copy()
        count_dict = dict()
        for name in selected_dropdown_value:
            count_dict[name] = datedf['Common_Name'].value_counts()[name]
        cdf = pd.DataFrame({
            'Bird': count_dict.keys(),
            'Count': count_dict.values()}
        )
    if graph_type == 'BAR':
        fig = px.bar(cdf, x='Bird', y='Count', title='Bar Graph', color='Bird', template='custom')
    elif graph_type == 'LINE':
        pd.set_option("display.max_rows", None, "display.max_columns", None)
        tbl = datedf.groupby(['Common_Name', 'Date']).agg({'Common_Name':'count'})
        tbl.index = tbl.index.set_names(['Bird', 'Date'])
        tbl.reset_index(inplace=True)
        tbl = tbl.rename(columns={'Common_Name': 'Count'})
        fig = px.line(tbl, x='Date', y='Count', color='Bird', title='Line Graph', template='custom')
    fig.update_layout(title={'y':0.9, 'x':0.45, 'xanchor': 'center'})
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)