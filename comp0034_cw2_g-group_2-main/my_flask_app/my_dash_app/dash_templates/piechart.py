import pandas as pd
import plotly.express as px
import data_preparation_functions as dp


def piechart_fig(country, year, category):

    df_data = pd.read_csv('prepared_df_data.csv')

    frames = []
    #for c in country:
        #filtered_data = df_data[(df_data['Country1 Code'] == c) & [(df_data['Country2 Code'] == c)]
        #frames.append(filtered_data)

    final_df = pd.concat(frames)
    input_year = str(year)
    input_category = str(category)

    fig = px.pie(df_pie, "Country Code", years, title=title)
    return fig


#COUNTRY = ['LTU', 'POL', 'DEU', 'FRA']
#YEAR = 2014
#CAT = 'Dealing with construction permits (DB06-15 methodology) - Score'

#fig = piechart_fig(COUNTRY, YEAR, CAT)
#fig.show()
