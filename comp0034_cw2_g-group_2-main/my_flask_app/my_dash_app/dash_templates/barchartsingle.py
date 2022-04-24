import pandas as pd
import plotly.express as px
import data_preparation_functions as dp


def barsingle_fun(countries, category, year):

    df_data = pd.read_csv('prepared_df_data.csv')

    df_names = countries

    for i in range(len(countries)):
        temp_df = dp.country_dataframe(countries[i], df_data)
        data = temp_df.index == category
        df_names[i] = pd.DataFrame(temp_df[data])

    combined = pd.concat(df_names)
    print(combined)

    inputYears = str(year)

    bars = pd.DataFrame(combined)
    print(bars)
    fig = px.bar(bars, x="Country Code", y=inputYears, color=inputYears, height=400, title="Score per country for year")
    return fig
