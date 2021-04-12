import pandas as pd
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from datetime import date
import plotly.io as plt_io
from app import app
import clustering

global df
global new_df
global dict_names
global new_dict_names

df = pd.read_csv("finalMergedBirds/finalbirdsSEM4.csv")
df['Date'] = pd.to_datetime(df['Date'])
# basebardf = df['Common_Name'].value_counts()

new_df = clustering.clusterset(df)
new_df['Date'] = pd.to_datetime(df['Date'])


def create_dict_list_of_product():
    dictlist = []
    unique_list = df.Common_Name.unique()
    for product_title in unique_list:
        dictlist.append({'value': product_title, 'label': product_title})
    return dictlist


def create_new_dict_list_of_products():
    dictlist = []
    unique_list = new_df.Cluster.unique()
    for product_title in unique_list:
        dictlist.append({'value': product_title, 'label': product_title})
    return dictlist


dict_names = create_dict_list_of_product()
new_dict_names = create_new_dict_list_of_products()

plt_io.templates['custom'] = plt_io.templates['plotly_dark']
plt_io.templates['custom']['layout']['paper_bgcolor'] = '#96dcd4'
plt_io.templates['custom']['layout']['plot_bgcolor'] = '#96dcd4'
plt_io.templates['custom']['layout']['font']['color'] = '#000000'
plt_io.templates['custom']['layout']['font']['color'] = '#000000'
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
stuff = dict()
for name in df['Common_Name']:
    stuff[name] = df['Common_Name'].value_counts()[name]
sdf = pd.DataFrame({
    'Common_Name': stuff.keys(),
    'Count': stuff.values()}
)
piec = px.pie(sdf, values='Count', names='Common_Name', title='Pie Chart', template='custom')
piec.update_traces(marker=dict(line=dict(color='#000000', width=0.5)))
piec.update_layout(title={'y': 0.9, 'x': 0.5, 'xanchor': 'center'})

new_stuff = dict()
for name in new_df['Cluster']:
    new_stuff[name] = new_df['Cluster'].value_counts()[name]
nsdf = pd.DataFrame({
    'Cluster': new_stuff.keys(),
    'Count': new_stuff.values()}
)
new_piec = px.pie(nsdf, values='Count', names='Cluster', title='Pie Chart', template='custom', )
new_piec.update_traces(marker=dict(line=dict(color='#000000', width=0.5)))
new_piec.update_layout(title={'y': 0.9, 'x': 0.5, 'xanchor': 'center'})

layout = html.Div([
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
            dcc.Tab(label='Species',style=tab_style, selected_style=tab_selected_style, children=[
                html.Div([
                    html.Div([
                        dcc.Dropdown(
                            id='graph-type',
                            options=[{'value': 'BAR', 'label': 'Bar'},
                                     {'value': 'LINE', 'label': 'Line'}],
                            value='BAR',
                        )
                    ], className='dropdownFrame',
                        style={'width': '11%', 'top': '80px', 'left': '34%', 'position': 'absolute',
                               'display': 'block'}),
                    # html.Div([
                        # dcc.Dropdown(
                            # id='product-dropdown',
                            # options=dict_names,
                            # multi=True,
                            # placeholder='Select Birds',
                        # )
                    # ], className='dropdownFrame',
                        # style={'width': '37%', 'top': '140px', 'left': '12%', 'position': 'absolute',
                               # 'display': 'block'}),
                    html.Div([
                        dcc.Graph(id='graphs')
                    ], style={'box-shadow': '2px 2px 2px black', 'top': '140px', 'left': '1%', 'width': '48%',
                              'position': 'absolute', 'display': 'block'}),
                    html.Div([
                        dcc.Graph(
                            id='pie',
                            figure=piec
                        )
                    ], style={'box-shadow': '2px 2px 2px black', 'top': '140px', 'left': '51%', 'width': '48%',
                              'position': 'absolute', 'display': 'block'}),
                    html.Div(className='CalendarFrame', children=[
                        dcc.DatePickerRange(min_date_allowed=date(2015, 1, 1),
                                            max_date_allowed=date(2020, 10, 25),
                                            initial_visible_month=date(2020, 10, 25),
                                            start_date=date(2015, 1, 1),
                                            end_date=date(2020, 10, 25),
                                            display_format='Do/MMM/YYYY',
                                            id="Date_Range")
                    ], style={'left': '1%', 'top': '70px', 'position': 'absolute', 'display': 'block'})
                ])
            ]),
            # end of Tab 1
            dcc.Tab(label='Clusters',style=tab_style, selected_style=tab_selected_style, children=[
                html.Div([
                    html.Div([
                        dcc.Dropdown(
                            id='new_graph-type',
                            options=[{'value': 'BAR', 'label': 'Bar'},
                                     {'value': 'LINE', 'label': 'Line'}],
                            value='BAR',
                        )
                    ], className='dropdownFrame',
                        style={'width': '11%', 'top': '80px', 'left': '34%', 'position': 'absolute',
                               'display': 'block'}),
                    # html.Div([
                        # dcc.Dropdown(
                            # id='new_product-dropdown',
                            # options=new_dict_names,
                            # multi=True,
                            # placeholder='Select Cluster',
                        # )
                    # ], className='dropdownFrame',
                        # style={'width': '37%', 'top': '140px', 'left': '12%', 'position': 'absolute',
                               # 'display': 'block'}),
                    html.Div([
                        dcc.Graph(id='new_graph')
                    ], style={'box-shadow': '2px 2px 2px black', 'top': '140px', 'left': '1%', 'width': '48%',
                              'position': 'absolute', 'display': 'block'}),
                    html.Div([
                        dcc.Graph(
                            id='pie',
                            figure=new_piec
                        )
                    ], style={'box-shadow': '2px 2px 2px black', 'top': '140px', 'left': '51%', 'width': '48%',
                              'position': 'absolute', 'display': 'block'}),
                    html.Div(className='CalendarFrame', children=[
                        dcc.DatePickerRange(min_date_allowed=date(2015, 1, 1),
                                            max_date_allowed=date(2020, 10, 25),
                                            initial_visible_month=date(2020, 10, 25),
                                            start_date=date(2015, 1, 1),
                                            end_date=date(2020, 10, 25),
                                            display_format='Do/MMM/YYYY',
                                            id="new_Date_Range")
                    ], style={'left': '1%', 'top': '70px', 'position': 'absolute', 'display': 'block'})
                ])
            ]),
            # end of tab 2
            dcc.Tab(label='Clusters and Species',style=tab_style, selected_style=tab_selected_style, children=[
                html.Div([
                    html.Div([
                        dcc.Dropdown(
                            id='c_s_product-dropdown',
                            options=new_dict_names,
                            multi=True,
                            placeholder='Select Cluster',
                        )
                    ], className='dropdownFrame',
                        style={'width': '48%', 'top': '140px', 'left': '1%', 'position': 'absolute',
                               'display': 'block'}),
                    html.Div([
                        dcc.Dropdown(
                            id='pie_product-dropdown',
                            options=new_dict_names,
                            value=new_dict_names[0]['value'],
                        )
                    ], className='dropdownFrame',
                        style={'width': '30%', 'top': '140px', 'left': '51%', 'position': 'absolute',
                               'display': 'block'}),
                    html.Div([
                        dcc.Graph(id='c_s_graph')
                    ], style={'box-shadow': '2px 2px 2px black', 'top': '230px', 'left': '1%', 'width': '48%',
                              'position': 'absolute', 'display': 'block'}),
                    html.Div([
                        dcc.Graph(id='c_s_pie')
                    ], style={'box-shadow': '2px 2px 2px black', 'top': '230px', 'left': '51%', 'width': '48%',
                              'position': 'absolute', 'display': 'block'}),
                    html.Div(className='CalendarFrame', children=[
                        dcc.DatePickerRange(min_date_allowed=date(2015, 1, 1),
                                            max_date_allowed=date(2020, 10, 25),
                                            initial_visible_month=date(2020, 10, 25),
                                            start_date=date(2015, 1, 1),
                                            end_date=date(2020, 10, 25),
                                            display_format='Do/MMM/YYYY',
                                            id="c_s_Date_Range")
                    ], style={'left': '1%', 'top': '70px', 'position': 'absolute', 'display': 'block'})
                ])
            ])
        ]),
        #end of tab3
    ], style={'top': '17%', 'left': '2.5%', 'width': '95%', 'display': 'block', 'position': 'absolute'}),
    html.Footer(
        ['© CMPN SE Group 6 2020-2021'],
        className='footer',
    )
], style={'background-color': '#449bb3', 'min-height': '1000px'})


# callback for bird graph
@app.callback(Output('graphs', 'figure'),
              [Input('Date_Range', 'start_date'), Input('Date_Range', 'end_date'), Input('graph-type', 'value')])
def generate_graph(start_date, end_date, graph_type):
    # if (selected_dropdown_value is None) or (len(selected_dropdown_value) == 0):
        # datedf = df[(df['Date'] < end_date) & (df['Date'] > start_date)].copy()
        # bruh = datedf['Common_Name'].value_counts()
        # cdf = dict()
        # for name, value in bruh.items():
            # cdf[name] = value
        # cdf = pd.DataFrame({
            # 'Bird': cdf.keys(),
            # 'Count': cdf.values()
        # })
    # else:
        # if type(selected_dropdown_value) is str:
            # xdf = df[df['Common_Name'] == selected_dropdown_value]
        # else:
            # xdf = df[(df['Common_Name'].isin(selected_dropdown_value))]
        # datedf = xdf[(xdf['Date'] < end_date) & (xdf['Date'] > start_date)].copy()
        # bruh = datedf['Common_Name'].value_counts()
        # cdf = dict()
        # for name, value in bruh.items():
            # cdf[name] = value
        # cdf = pd.DataFrame({
            # 'Bird': cdf.keys(),
            # 'Count': cdf.values()}
        # )
    datedf = df[(df['Date'] < end_date) & (df['Date'] > start_date)].copy()
    if graph_type == 'BAR':
        bruh = datedf['Common_Name'].value_counts()
        cdf = dict()
        for name, value in bruh.items():
            cdf[name] = value
        cdf = pd.DataFrame({
            'Bird': cdf.keys(),
            'Count': cdf.values()
        })
        fig = px.bar(cdf, x='Bird', y='Count', title='Bar Graph', color='Bird', template='custom')
    elif graph_type == 'LINE':
        pd.set_option("display.max_rows", None, "display.max_columns", None)
        tbl = datedf.groupby(['Common_Name', 'Date']).agg({'Common_Name': 'count'})
        tbl.index = tbl.index.set_names(['Bird', 'Date'])
        tbl.reset_index(inplace=True)
        tbl = tbl.rename(columns={'Common_Name': 'Count'})
        fig = px.line(tbl, x='Date', y='Count', color='Bird', title='Line Graph', template='custom')
    fig.update_layout(title={'y': 0.9, 'x': 0.45, 'xanchor': 'center'})
    return fig


# call back for cluster graph
@app.callback(Output('new_graph', 'figure'),
              [Input('new_Date_Range', 'start_date'), Input('new_Date_Range', 'end_date'), Input('new_graph-type', 'value')])
def generate_graph(start_date, end_date, graph_type):
    # if (selected_dropdown_value is None) or (len(selected_dropdown_value) == 0):
        # datedf = new_df[(new_df['Date'] < end_date) & (new_df['Date'] > start_date)].copy()
        # bruh = datedf['Cluster'].value_counts()
        # cdf = dict()
        # for name, value in bruh.items():
            # cdf[name] = value
        # cdf = pd.DataFrame({
            # 'Cluster': cdf.keys(),
            # 'Count': cdf.values()
        # })
    # else:
        # if type(selected_dropdown_value) is str:
            # xdf = new_df[new_df['Cluster'] == selected_dropdown_value]
        # else:
            # xdf = new_df[(new_df['Cluster'].isin(selected_dropdown_value))]
        # datedf = xdf[(xdf['Date'] < end_date) & (xdf['Date'] > start_date)].copy()
        # bruh = datedf['Cluster'].value_counts()
        # cdf = dict()
        # for name, value in bruh.items():
            # cdf[name] = value
        # cdf = pd.DataFrame({
            # 'Cluster': cdf.keys(),
            # 'Count': cdf.values()}
        # )
    datedf = new_df[(new_df['Date'] < end_date) & (new_df['Date'] > start_date)].copy()
    if graph_type == 'BAR':
        bruh = datedf['Cluster'].value_counts()
        cdf = dict()
        for name, value in bruh.items():
            cdf[name] = value
        cdf = pd.DataFrame({
            'Cluster': cdf.keys(),
            'Count': cdf.values()
        })
        fig = px.bar(cdf, x='Cluster', y='Count', title='Bar Graph', color='Cluster', template='custom')
    elif graph_type == 'LINE':
        pd.set_option("display.max_rows", None, "display.max_columns", None)
        tbl = datedf.groupby(['Cluster', 'Date']).agg({'Cluster': 'count'})
        tbl.index = tbl.index.set_names(['cluster', 'Date'])
        tbl.reset_index(inplace=True)
        tbl = tbl.rename(columns={'Cluster': 'Count', 'cluster': 'Cluster'})
        fig = px.line(tbl, x='Date', y='Count', color='Cluster', title='Line Graph', template='custom')
    fig.update_layout(title={'y': 0.9, 'x': 0.45, 'xanchor': 'center'})
    return fig
    
#callback for species_cluster graph
@app.callback(Output('c_s_graph','figure'),
              [Input('c_s_Date_Range','start_date'), Input('c_s_Date_Range','end_date'),
               Input('c_s_product-dropdown','value')])
def generate_graph(start_date, end_date,selected_dropdown_value=None):
    if (selected_dropdown_value is None) or (len(selected_dropdown_value) == 0):
        xdf = new_df
    elif type(selected_dropdown_value) is str:
        xdf = new_df[new_df['Cluster'] == selected_dropdown_value]
    else:
        xdf = new_df[(new_df['Cluster'].isin(selected_dropdown_value))]
    datedf = xdf[(xdf['Date'] < end_date) & (xdf['Date'] > start_date)].copy()
    tbl = datedf.groupby(['Cluster','Common_Name']).agg({'Common_Name':'count'})
    tbl.index = tbl.index.set_names(['Cluster','Bird'])
    tbl.reset_index(inplace=True)
    tbl = tbl.rename(columns={'Common_Name':'Count'})
    fig = px.bar(tbl, x='Cluster', y='Count', color='Bird', title='Bar Graph', template='custom')
    fig.update_layout(title={'y': 0.9, 'x': 0.45, 'xanchor': 'center'})
    return fig

#callback for species_cluster pie
@app.callback(Output('c_s_pie','figure'),Input('pie_product-dropdown','value'))
def generate_graph(selected_dropdown_value):
    xdf = new_df[new_df['Cluster'] == selected_dropdown_value]
    xstuff = dict()
    for name in xdf['Common_Name']:
        xstuff[name] = xdf['Common_Name'].value_counts()[name]
    ndf = pd.DataFrame({
        'Birds': xstuff.keys(),
        'Count': xstuff.values()
    })
    fig = px.pie(ndf, names='Birds', values='Count', title='Pie Chart',template='custom')
    fig.update_traces(marker=dict(line=dict(color='#000000', width=0.5)))
    fig.update_layout(title={'y': 0.9, 'x': 0.5, 'xanchor': 'center'})
    return fig

