import dash
from matplotlib.pyplot import title
import pandas as pd
from dash import html, dcc
import data_preparation
import plotly.express as px
import data_preparation_functions as dp
import numpy as np
import plotly.figure_factory as ff

#should i add it to setup?

# Countries and years selected by the user on the web app, provides inputs
countries = ["France", "Lithuania", "Poland", "Germany"]
category = "Dealing with construction permits (DB06-15 methodology) - Score"
years = ['2014','2015']

def table_func(countries, category, years):

    df_data = pd.read_csv('prepared_df_data.csv')

    df_names = countries


    for i in range(len(countries)):
        temp_df = dp.country_dataframe(countries[i], df_data)
        data = temp_df.index == category
        df_names[i] = pd.DataFrame(temp_df[data])

    combined = pd.concat(df_names)

    print(combined)

    tablee = pd.DataFrame(combined)
    fig = ff.create_table(tablee)
    
    return fig

