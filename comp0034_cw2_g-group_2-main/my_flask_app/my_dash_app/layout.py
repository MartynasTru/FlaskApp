from pathlib import Path

import numpy as np
import pandas as pd
from dash import dcc, html

data_path = Path(__file__).parent.parent.parent.joinpath('my_flask_app', 'my_dash_app', 'data', 'prepared_df_data.csv')
df = pd.read_csv(data_path)

# data_url = 'https://drive.google.com/file/d/14_IGuPvcBPpNqta23Iwk1r-ZyCXS4JRX/view?usp=sharing'
# data_url = 'https://drive.google.com/uc?id=' + data_url.split('/')[-2]
# df = pd.read_csv(data_url)

country_codeList = np.unique(df["Country Code"].tolist()).tolist()
categoryList = np.unique(df["Indicator Name"].tolist()).tolist()
yearList = [2014, 2015, 2016, 2017, 2018, 2019, 2020]
stryearList = ['2014', '2015', '2016', '2017', '2018', '2019', '2020']

pie_tab = html.Div([
    html.H3('Pie chart', style={
        'font-size': '30px', 'margin-bottom': '5px', 'font-family': 'monospace'}),
    html.H4('Please select one year, one category and a number of countries.',
            style={'font-size': '15px', 'margin-bottom': '15px', 'font-family': 'monospace'}),
    dcc.RadioItems(id='pie_year_radio', options=[{'label': v, 'value': v} for v in stryearList],
                   labelStyle={'display': 'inline-block'}),
    html.Div([], style={'marginBottom': '1em'}),
    dcc.Dropdown(id='pie_dd', options=[
        {'label': v, 'value': v} for v in country_codeList], multi=True),
    dcc.Dropdown(id='pie_category_radio',
                 options=[{'label': v, 'value': v} for v in categoryList], multi=False),
    html.Div(id='pie_chart'),
    html.H4('If a title but no chart appears, there is no available data that meets the selected parameters.',
            style={'font-size': '10px', 'margin-bottom': '10px', 'font-family': 'monospace'}),
    html.A(html.Button('Back to the Home page'), href='/'),
    html.A(html.Button('Download the data', id="btn_csv"), href='/downloadpie')],
    style={'width': '90%', 'margin-left': '80px', 'margin-right': "25px",
           'margin-top': "30px", 'textAlign': 'center'})

single_bar_tab = html.Div([
    html.H3('Bar chart single',
            style={'font-size': '30px', 'margin-bottom': '10px', 'font-family': 'monospace'}),
    html.H4('Please select one year, one category and a number of countries.',
            style={'font-size': '15px', 'margin-bottom': '15px', 'font-family': 'monospace'}),
    dcc.RadioItems(id='single_bar_year', options=[{'label': v, 'value': v} for v in stryearList],
                   labelStyle={'display': 'inline-block'}),
    html.Div([], style={'marginBottom': '1em'}),
    dcc.Dropdown(id='single_bar_code', options=[{'label': v, 'value': v} for v in country_codeList],
                 multi=True),
    dcc.Dropdown(id='single_bar_category', options=[{'label': v, 'value': v} for v in categoryList],
                 multi=False),
    html.Div(id='single_bar'),
    html.H4('If a title but no chart appears, there is no available data that meets the selected parameters.',
            style={'font-size': '10px', 'margin-bottom': '10px', 'font-family': 'monospace'}),
    html.A(html.Button('Back to the Home page'), href='/'),
    html.A(html.Button('Download the data', id="btn_csv"), href='/downloadsingle')],
    style={'width': '90%', 'margin-left': '80px', 'margin-right': "25px",
           'margin-top': "30px", 'textAlign': 'center'})

multi_bar_tab = html.Div([
    html.H3('Multi bar chart single',
            style={'font-size': '30px', 'margin-bottom': '10px', 'font-family': 'monospace'}),
    html.H4('Please select one category and a number of years and countries.',
            style={'font-size': '15px', 'margin-bottom': '15px', 'font-family': 'monospace'}),
    dcc.Checklist(id='multi_bar_year', options=[{'label': v, 'value': v} for v in stryearList],
                  labelStyle={'display': 'inline-block'}),
    html.Div([], style={'marginBottom': '1em'}),
    dcc.Dropdown(id='multi_bar_code', options=[
        {'label': v, 'value': v} for v in country_codeList], multi=True),
    dcc.Dropdown(id='multi_bar_category', options=[
        {'label': v, 'value': v} for v in categoryList], multi=False),
    html.Div(id='multi_bar'),
    html.H4('If a title but no chart appears, there is no available data that meets the selected parameters.',
            style={'font-size': '10px', 'margin-bottom': '10px', 'font-family': 'monospace'}),
    html.A(html.Button('Back to the Home page'), href='/'),
    html.A(html.Button('Download the data', id="btn_csv"), href='/downloadmulti')],
    style={'width': '90%', 'margin-left': '80px', 'margin-right': "25px",
           'margin-top': "30px", 'textAlign': 'center'})

table_tab = html.Div([
    html.H3('Table', style={'font-size': '30px',
                            'margin-bottom': '10px', 'font-family': 'monospace'}),
    html.H4('Please select one category and a number of years and countries.',
            style={'font-size': '15px', 'margin-bottom': '15px', 'font-family': 'monospace'}),
    dcc.Checklist(id='table_year', options=[{'label': v, 'value': v} for v in stryearList],
                  labelStyle={'display': 'inline-block'}),
    html.Div([], style={'marginBottom': '1em'}),
    dcc.Dropdown(id='table_code', options=[
        {'label': v, 'value': v} for v in country_codeList], multi=True),
    dcc.Dropdown(id='table_category', options=[
        {'label': v, 'value': v} for v in categoryList], multi=False),
    html.Div(id='table_data'),
    html.H4('If a title but no chart appears, there is no available data that meets the selected parameters.',
            style={'font-size': '10px', 'margin-bottom': '10px', 'font-family': 'monospace'}),
    html.A(html.Button('Back to the Home page'), href='/'),
    html.A(html.Button('Download the data', id="btn_csv"), href='/downloadtable')],
    style={'width': '90%', 'margin-left': '80px', 'margin-right': "25px",
           'margin-top': "30px", 'textAlign': 'center'})

heatmap_tab = html.Div([
    html.H3('Heatmap', style={'font-size': '30px',
                              'margin-bottom': '10px', 'font-family': 'monospace'}),
    html.H4('Please select up to four years, one category and a number of countries.',
            style={'font-size': '15px', 'margin-bottom': '15px', 'font-family': 'monospace'}),
    dcc.Checklist(id='heatmap_year', options=[{'label': v, 'value': v} for v in stryearList],
                  labelStyle={'display': 'inline-block'}),
    html.Div([], style={'marginBottom': '1em'}),
    dcc.Dropdown(id='heatmap_code', options=[
        {'label': v, 'value': v} for v in country_codeList], multi=True),
    dcc.Dropdown(id='heatmap_category', options=[
        {'label': v, 'value': v} for v in categoryList], multi=False),
    html.Div(id='heatmap_data'),
    html.H4('If a title but no chart appears, there is no available data that meets the selected parameters.',
            style={'font-size': '10px', 'margin-bottom': '10px', 'font-family': 'monospace'}),
    html.A(html.Button('Back to the Home page'), href='/'),
    html.A(html.Button('Download the data', id="btn_csv"), href='/downloadheat')],
    style={'width': '90%', 'margin-left': '80px', 'margin-right':
        "25px", 'margin-top': "30px", 'textAlign': 'center'})

layout = html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Pie chart', value='tab-1'),
        dcc.Tab(label='Bar chart single', value='tab-2'),
        dcc.Tab(label='Bar chart multiple', value='tab-3'),
        dcc.Tab(label='Table', value='tab-4'),
        dcc.Tab(label='Heatmap (matrix)', value='tab-5')],
             style={'textAlign': 'center',
                    'border': '2px solid blue'}), html.Div(id='tabs-content')])
