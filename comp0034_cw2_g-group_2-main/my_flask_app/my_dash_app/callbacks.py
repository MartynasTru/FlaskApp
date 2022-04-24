from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import dcc
from dash.dependencies import Input, Output
from my_dash_app import layout


def register_callbacks(app):
    @app.callback(Output('tabs-content', 'children'),
                  Input('tabs', 'value'))
    def render_content(tab):
        if tab == 'tab-1':
            return layout.pie_tab
        elif tab == 'tab-2':
            return layout.single_bar_tab
        elif tab == 'tab-3':
            return layout.multi_bar_tab
        elif tab == 'tab-4':
            return layout.table_tab
        elif tab == 'tab-5':
            return layout.heatmap_tab

    @app.callback(
        # Pie chart callback
        Output('pie_chart', 'children'),
        Input('pie_dd', 'value'),
        Input('pie_year_radio', 'value'),
        Input('pie_category_radio', 'value'))
    def display_pie(country, year, category):
        if country and year and category is not None:

            data_path = Path(__file__).parent.parent.parent.joinpath('my_flask_app', 'my_dash_app', 'data',
                                                                     'prepared_df_data.csv')
            df_data = pd.read_csv(data_path)
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

            fig.write_image("images/piechart.png", engine="kaleido")

            return dcc.Graph(figure=fig)

    @app.callback(
        # Single-bar chart callback
        Output('single_bar', 'children'),
        Input('single_bar_code', 'value'),
        Input('single_bar_year', 'value'),
        Input('single_bar_category', 'value'))
    def display_single_bar(country, year, category):
        if country and year and category is not None:

            data_path = Path(__file__).parent.parent.parent.joinpath('my_flask_app', 'my_dash_app', 'data',
                                                                     'prepared_df_data.csv')
            df_data = pd.read_csv(data_path)

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

            bars.write_image("images/singlebar.png", engine="kaleido")

            return dcc.Graph(figure=bars)

    @app.callback(
        # Multiple-bar chart callback
        Output('multi_bar', 'children'),
        Input('multi_bar_code', 'value'),
        Input('multi_bar_year', 'value'),
        Input('multi_bar_category', 'value'))
    def display_multi_bar(country, year, category):
        if country and year and category is not None:

            data_path = Path(__file__).parent.parent.parent.joinpath('my_flask_app', 'my_dash_app', 'data',
                                                                     'prepared_df_data.csv')
            df_data = pd.read_csv(data_path)
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
            multibars.write_image("images/picture1.png", engine="kaleido")

            multibars.write_image("images/multibars.png", engine="kaleido")

            return dcc.Graph(figure=multibars)

    @app.callback(
        # Table callback
        Output('table_data', 'children'),
        Input('table_code', 'value'),
        Input('table_year', 'value'),
        Input('table_category', 'value'))
    def display_table(country, year, category):
        if country and year and category is not None:

            data_path = Path(__file__).parent.parent.parent.joinpath('my_flask_app', 'my_dash_app', 'data',
                                                                     'prepared_df_data.csv')
            df_data = pd.read_csv(data_path)
            frames = []

            for c in country:
                filtered_data = df_data[(df_data['Country Code'] == c) & (
                        df_data['Indicator Name'] == category)]
                frames.append(filtered_data)

            final_df = pd.concat(frames)

            input_year = str(year)
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
            fig.write_image("images/table.png", engine="kaleido")

            # fig.write_image("/images/fig1.png")
            return dcc.Graph(figure=fig)

    @app.callback(
        # Heatmap callback
        Output('heatmap_data', 'children'),
        Input('heatmap_code', 'value'),
        Input('heatmap_year', 'value'),
        Input('heatmap_category', 'value'))
    def display_heatmap(country, year, category):
        if country and year and category is not None:
            data_path = Path(__file__).parent.parent.parent.joinpath('my_flask_app', 'my_dash_app', 'data',
                                                                     'prepared_df_data.csv')
            df_data = pd.read_csv(data_path)
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

            fig.write_image("images/heatmap.png", engine="kaleido")

            return dcc.Graph(figure=fig)
