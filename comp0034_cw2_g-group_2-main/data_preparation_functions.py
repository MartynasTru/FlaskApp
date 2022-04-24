import pandas as pd


# Now we have the prepared dataframe for all countries
# However, to make visualisations we only need dataframes for select countries
def country_dataframe(country_code, data_df):
    # Reformatting the data of interest into new dataframes
    data = data_df['Country Code'] == country_code
    df_data_new = pd.DataFrame(data_df[data])
    # Removing redundant information
    df_data_new = df_data_new.iloc[:, 2:]
    df_data_new.set_index('Indicator Name', inplace=True)
    return df_data_new


def df_to_plotly(df):
    return {'z': df.values.tolist(),
            'x': df.columns.tolist(),
            'y': df.index.tolist()}


def filter_list(list):
    temp = []
    for items in list:
        if str == type(items):
            temp.append(items)
    for item_to_remove in temp:
        list.remove(item_to_remove)
    return list


def year_selection(availableYears, userYears):
    pos1 = availableYears.index(userYears[0])
    if len(userYears) > 1:
        pos2 = availableYears.index(userYears[-1])
        return pos1, pos2
    else:
        return pos1



