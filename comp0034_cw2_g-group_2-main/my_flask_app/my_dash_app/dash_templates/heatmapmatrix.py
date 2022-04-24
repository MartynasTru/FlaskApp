import plotly.express as px
import pandas as pd
import data_preparation_functions as dp


def heatmap_func(countries, category, years):

    availableYears = [2014, 2015, 2016, 2017, 2018, 2019, 2020]
    yearIndex = dp.year_selection(availableYears, years)

    df_data = pd.read_csv('prepared_df_data.csv')

    df_names = countries

    for i in range(len(countries)):
        temp_df = dp.country_dataframe(countries[i], df_data)
        data = temp_df.index == category
        df_names[i] = pd.DataFrame(temp_df[data])

    combined = pd.concat(df_names)

    dict1 = {}
    dict1 = dp.df_to_plotly(combined)

    dataZ = {}

    for i in range(len(dict1['z'])):
        dataZ[i] = dp.filter_list(dict1['z'][i])

    listZ = [[] for i in range(len(dataZ))]

    for y in range(len(dataZ)):
        if len(yearIndex) > 1:
            listZ[y] = (dataZ[y][yearIndex[0]:yearIndex[1]+1])
        else:
            listZ[y] = (dataZ[y][yearIndex[0]])

    title = category + " | Heatmap of the countries' score over select years"

    fig = px.imshow(listZ, x=years, y=countries)

    fig.update_layout(title_text=title, yaxis={"title": 'Country'}, xaxis={"title": 'Years'},
                      yaxis_nticks=len(countries), xaxis_nticks=len(years))
    return fig


def display_heatmap(country, year, category):
    if country and year and category is not None:
        if len(year) > 4:
            print("COUNTRY1: ", country)
            print("YEAR: ", year)
            print("CAT: ", category)
            return "Please do not select more than four years"
        else:
            print("COUNTRY2: ", country)
            print("YEAR: ", year)
            print("CAT: ", category)

            df_data = pd.read_csv('prepared_df_data.csv')
            frames = []

            for c in country:
                filtered_data = df_data[(df_data['Country Code'] == c) & (df_data['Indicator Name'] == category)]
                frames.append(filtered_data)

            final_df = pd.concat(frames)

            input_year = str(year)
            string_array = ["Country Code"]
            for y in year:
                string_array.append(y)

            final_df = final_df[string_array]
            final_df.set_index('Country Code', inplace=True)
            temp_df = final_df
            final_df = final_df[:].values
            matrix_list = final_df.tolist()

            fig = px.imshow(matrix_list, x=year, y=country)

            title = category + " | Heatmap of the countries' score over select years"
            fig.update_layout(title_text=title, yaxis={"title": 'Country'}, xaxis={"title": 'Years'},
                              xaxis_nticks=len(year), yaxis_nticks=len(country))

            return temp_df


year = ['2014', '2015', '2016', '2017']
country = ['FRA', 'DEU', 'LTU', 'POL']
category = "Dealing with construction permits (DB06-15 methodology) - Score"

fig = display_heatmap(country, year, category)
print(fig)
#fig.show()

