import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

df = pd.read_csv('prepared_df_data.csv')

country_codeList = np.unique(df["Country Code"].tolist()).tolist()
categoryList = np.unique(df["Indicator Name"].tolist()).tolist()
yearList = [2014, 2015, 2016, 2017, 2018, 2019, 2020]
stryearList = ['2014', '2015', '2016', '2017', '2018', '2019', '2020']

app = Dash(__name__, suppress_callback_exceptions=True)

pie_tab = html.Div([
    html.H3('Pie chart', style={
        'font-size': '30px', 'margin-bottom': '5px', 'font-family': 'monospace'}),
    html.H4('Please select one year, one category and a number of countries.',
            style={'font-size': '15px', 'margin-bottom': '15px', 'font-family': 'monospace'}),
    dcc.RadioItems(id='pie_year_radio', options=[{'label': v, 'value': v} for v in stryearList],
                   labelStyle={'display': 'inline-block'}),
    dcc.Dropdown(id='pie_dd', options=[
        {'label': v, 'value': v} for v in country_codeList], multi=True),
    dcc.Dropdown(id='pie_category_radio',
                 options=[{'label': v, 'value': v} for v in categoryList], multi=False),
    html.Div(id='pie_chart'),
    html.H4('If a title but no chart appears, there is no available data that meets the selected parameters.',
            style={'font-size': '10px', 'margin-bottom': '10px', 'font-family': 'monospace'})
],
    style={'width': '90%', 'margin-left': '80px', 'margin-right': "25px",
           'margin-top': "30px", 'textAlign': 'center'})

single_bar_tab = html.Div([
    html.H3('Bar chart single',
            style={'font-size': '30px', 'margin-bottom': '10px', 'font-family': 'monospace'}),
    html.H4('Please select one year, one category and a number of countries.',
            style={'font-size': '15px', 'margin-bottom': '15px', 'font-family': 'monospace'}),
    dcc.RadioItems(id='single_bar_year', options=[{'label': v, 'value': v} for v in stryearList],
                   labelStyle={'display': 'inline-block'}),
    dcc.Dropdown(id='single_bar_code', options=[{'label': v, 'value': v} for v in country_codeList],
                 multi=True),
    dcc.Dropdown(id='single_bar_category', options=[{'label': v, 'value': v} for v in categoryList],
                 multi=False),
    html.Div(id='single_bar'),
    html.H4('If a title but no chart appears, there is no available data that meets the selected parameters.',
            style={'font-size': '10px', 'margin-bottom': '10px', 'font-family': 'monospace'})
],
    style={'width': '90%', 'margin-left': '80px', 'margin-right': "25px",
           'margin-top': "30px", 'textAlign': 'center'})

multi_bar_tab = html.Div([
    html.H3('Multi bar chart single',
            style={'font-size': '30px', 'margin-bottom': '10px', 'font-family': 'monospace'}),
    html.H4('Please select one category and a number of years and countries.',
            style={'font-size': '15px', 'margin-bottom': '15px', 'font-family': 'monospace'}),
    dcc.Checklist(id='multi_bar_year', options=[{'label': v, 'value': v} for v in stryearList],
                  labelStyle={'display': 'inline-block'}),
    dcc.Dropdown(id='multi_bar_code', options=[
        {'label': v, 'value': v} for v in country_codeList], multi=True),
    dcc.Dropdown(id='multi_bar_category', options=[
        {'label': v, 'value': v} for v in categoryList], multi=False),
    html.Div(id='multi_bar'),
    html.H4('If a title but no chart appears, there is no available data that meets the selected parameters.',
            style={'font-size': '10px', 'margin-bottom': '10px', 'font-family': 'monospace'})
],
    style={'width': '90%', 'margin-left': '80px', 'margin-right': "25px",
           'margin-top': "30px", 'textAlign': 'center'})

table_tab = html.Div([
    html.H3('Table', style={'font-size': '30px',
                            'margin-bottom': '10px', 'font-family': 'monospace'}),
    html.H4('Please select one category and a number of years and countries.',
            style={'font-size': '15px', 'margin-bottom': '15px', 'font-family': 'monospace'}),
    dcc.Checklist(id='table_year', options=[{'label': v, 'value': v} for v in stryearList],
                  labelStyle={'display': 'inline-block'}),
    dcc.Dropdown(id='table_code', options=[
        {'label': v, 'value': v} for v in country_codeList], multi=True),
    dcc.Dropdown(id='table_category', options=[
        {'label': v, 'value': v} for v in categoryList], multi=False),
    html.Div(id='table_data'),
    html.H4('If a title but no chart appears, there is no available data that meets the selected parameters.',
            style={'font-size': '10px', 'margin-bottom': '10px', 'font-family': 'monospace'})
],
    style={'width': '90%', 'margin-left': '80px', 'margin-right': "25px",
           'margin-top': "30px", 'textAlign': 'center'})

heatmap_tab = html.Div([
    html.H3('Heatmap', style={'font-size': '30px',
                              'margin-bottom': '10px', 'font-family': 'monospace'}),
    html.H4('Please select up to four years, one category and a number of countries.',
            style={'font-size': '15px', 'margin-bottom': '15px', 'font-family': 'monospace'}),
    dcc.Checklist(id='heatmap_year', options=[{'label': v, 'value': v} for v in stryearList],
                  labelStyle={'display': 'inline-block'}),
    dcc.Dropdown(id='heatmap_code', options=[
        {'label': v, 'value': v} for v in country_codeList], multi=True),
    dcc.Dropdown(id='heatmap_category', options=[
        {'label': v, 'value': v} for v in categoryList], multi=False),
    html.Div(id='heatmap_data'),
    html.H4('If a title but no chart appears, there is no available data that meets the selected parameters.',
            style={'font-size': '10px', 'margin-bottom': '10px', 'font-family': 'monospace'})
],
    style={'width': '90%', 'margin-left': '80px', 'margin-right':
        "25px", 'margin-top': "30px", 'textAlign': 'center'})

layout = app.layout = html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Pie chart', value='tab-1'),
        dcc.Tab(label='Bar chart single', value='tab-2'),
        dcc.Tab(label='Bar chart multiple', value='tab-3'),
        dcc.Tab(label='Table', value='tab-4'),
        dcc.Tab(label='Heatmap (matrix)', value='tab-5')],
             style={'textAlign': 'center',
                    'border': '2px solid blue'}), html.Div(id='tabs-content')])


@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return pie_tab
    elif tab == 'tab-2':
        return single_bar_tab
    elif tab == 'tab-3':
        return multi_bar_tab
    elif tab == 'tab-4':
        return table_tab
    elif tab == 'tab-5':
        return heatmap_tab


@app.callback(
    # Pie chart callback
    Output('pie_chart', 'children'),
    Input('pie_dd', 'value'),
    Input('pie_year_radio', 'value'),
    Input('pie_category_radio', 'value'))
def display_pie(country, year, category):
    if country and year and category is not None:

        df_data = pd.read_csv('prepared_df_data.csv')
        frames = []

        for c in country:
            filtered_data = df_data[df_data['Country Code'] == c]
            frames.append(filtered_data)
        final_df = pd.concat(frames)
        input_year = str(year)
        input_category = str(category)

        final_df = final_df[["Country Code", "Indicator Name", input_year]]
        final_df = final_df[final_df['Indicator Name'] == input_category]

        title = category + " | Pie chart of the countries' proportional scores"

        fig = px.pie(final_df, "Country Code", year, title=title)
        fig.update_layout(title_x=0.5)

        return dcc.Graph(figure=fig)


@app.callback(
    # Single-bar chart callback
    Output('single_bar', 'children'),
    Input('single_bar_code', 'value'),
    Input('single_bar_year', 'value'),
    Input('single_bar_category', 'value'))
def display_single_bar(country, year, category):
    if country and year and category is not None:

        df_data = pd.read_csv('prepared_df_data.csv')

        frames = []
        for c in country:
            filtered_data = df_data[df_data["Country Code"] == c]
            frames.append(filtered_data)

        final_df = pd.concat(frames)
        input_year = str(year)
        input_category = str(category)

        final_df = final_df[["Country Code", "Indicator Name", input_year]]
        final_df = final_df[final_df['Indicator Name'] == input_category]

        title = category + " | Single-bar chart of the countries' scores"

        bars = px.bar(final_df, x="Country Code",
                      y=input_year, height=400, title=title)
        bars.update_layout(title_x=0.5, yaxis={"title": 'Score'})

        return dcc.Graph(figure=bars)


@app.callback(
    # Multiple-bar chart callback
    Output('multi_bar', 'children'),
    Input('multi_bar_code', 'value'),
    Input('multi_bar_year', 'value'),
    Input('multi_bar_category', 'value'))
def display_multi_bar(country, year, category):
    if country and year and category is not None:

        df_data = pd.read_csv('prepared_df_data.csv')
        frames = []

        for c in country:
            filtered_data = df_data[df_data["Country Code"] == c]
            frames.append(filtered_data)

        final_df = pd.concat(frames)
        input_year = []
        for y in year:
            input_year.append(y)

        input_category = str(category)

        string_array = ["Country Code", "Indicator Name"]
        for y in year:
            string_array.append(y)

        final_df = final_df[string_array]
        final_df = final_df[final_df['Indicator Name'] == input_category]

        title = category + " | Multiple-bar chart of the countries' scores"

        multibars = px.bar(final_df, x="Country Code",
                           y=input_year, barmode='group', title=title)
        multibars.update_layout(
            title_x=0.5, yaxis={"title": 'Score'}, legend_title="Selected Years")

        return dcc.Graph(figure=multibars)


@app.callback(
    # Table callback
    Output('table_data', 'children'),
    Input('table_code', 'value'),
    Input('table_year', 'value'),
    Input('table_category', 'value'))
def display_table(country, year, category):
    if country and year and category is not None:

        df_data = pd.read_csv('prepared_df_data.csv')
        frames = []

        for c in country:
            filtered_data = df_data[(df_data['Country Code'] == c) & (
                    df_data['Indicator Name'] == category)]
            frames.append(filtered_data)

        final_df = pd.concat(frames)

        str(year)
        string_array = ["Country Code"]
        for y in year:
            string_array.append(y)

        final_df = final_df[string_array]

        title = category + " | Table of the countries' scores"

        fig = go.Figure(data=[go.Table(
            header=dict(values=list(final_df.columns),
                        fill_color='paleturquoise', align='left'),
            cells=dict(values=final_df.transpose().values.tolist(), fill_color='lavender', align='left'))],
            layout=go.Layout(title=title))

        fig.update_layout(title_x=0.5)

        return dcc.Graph(figure=fig)


@app.callback(
    # Heatmap callback
    Output('heatmap_data', 'children'),
    Input('heatmap_code', 'value'),
    Input('heatmap_year', 'value'),
    Input('heatmap_category', 'value'))
def display_heatmap(country, year, category):
    if country and year and category is not None:
        df_data = pd.read_csv('prepared_df_data.csv')
        frames = []

        for c in country:
            filtered_data = df_data[(df_data['Country Code'] == c) & (
                    df_data['Indicator Name'] == category)]
            frames.append(filtered_data)

        final_df = pd.concat(frames)

        string_array = ["Country Code"]

        for y in year:
            string_array.append(y)

        final_df = final_df[string_array]
        final_df.set_index('Country Code', inplace=True)
        final_df = final_df[:].values
        matrix_list = final_df.tolist()

        fig = px.imshow(matrix_list, x=year, y=country)

        title = category + " | Heatmap of the countries' score over select years"
        fig.update_layout(title_text=title, yaxis={"title": 'Country'}, xaxis={"title": 'Years'},
                          xaxis_nticks=len(year), yaxis_nticks=len(country), title_x=0.5)

        return dcc.Graph(figure=fig)


if __name__ == "__main__":
    app.run_server(debug=True, port=8888)
