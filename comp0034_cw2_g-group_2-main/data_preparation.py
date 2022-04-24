import pandas as pd


# Function that removes blank spaces from 'object' columns
def blank_space_remover(df):
    for i in df.columns:
        # checking the datatype of each column
        if df[i].dtype == 'object':
            try:
                # applying strip function on column
                df[i] = df[i].map(str.strip)
            except TypeError:
                pass
        else:
            pass


# Function that drops columns with more than 50% null values
def null_column_remover(df):
    half_count = len(df)/2
    df = df.dropna(thresh=half_count, axis=1)
    return df


# Opening each page of the spreadsheet as a unique dataframe
df_data = pd.read_excel('DBEXCEL.xlsx', sheet_name='Data')
df_country = pd.read_excel('DBEXCEL.xlsx', sheet_name='Country')
df_series = pd.read_excel('DBEXCEL.xlsx', sheet_name='Series')

print('COLUMNS', df_data.columns)

# Display initial number of rows and columns of each dataframe
print('Data df shape: ', df_data.shape)
print('Country df shape: ', df_country.shape)
print('Series df shape: ', df_series.shape)

# Display proportion of null entries in each column
print('Proportion of null results in Data dataframe:', '\n', df_data.isnull().sum() / len(df_data), '\n')
# Removing the columns representing years 2004 to 2013 by calling function
df_data = null_column_remover(df_data)
# Removing blank spaces from 'object' columns by calling function
blank_space_remover(df_data)
# Drop unnecessary column
df_data = df_data.drop(['Indicator Code'], axis=1)

# Similar process for "Country" dataframe
print('Proportion of null results in Country dataframe:', '\n', df_country.isnull().sum() / len(df_country), '\n')
df_country = null_column_remover(df_country)
blank_space_remover(df_country)

# Similar process for "Series" dataframe
print('Proportion of null results in Series dataframe:', '\n', df_series.isnull().sum() / len(df_series), '\n')
df_series = null_column_remover(df_series)
blank_space_remover(df_series)
# From these outputs, we can see that the "Series" dataframe will not be useful in the data exploration

# Display unique entries in "Data"'s "Country Name" column
print('Unique countries/cities in "Data": ', '\n', df_data['Country Name'].unique(), '\n')

# Column "Country name" also contains the names of the 22 largest cities, which aren't necessary
# Removing 4509 first rows which represent the 22 cities using the iloc function to select the rest
df_data = df_data.iloc[4510:]

# Displaying unique countries again
print('Unique countries in "Data": ', '\n', df_data['Country Name'].unique(), '\n')

# Display remaining columns
print('"Data" columns: ', '\n', df_data.columns, '\n')
# Display rows with duplicates
print('Duplicates:', '\n', df_data.duplicated(), '\n')
# Show data type of columns
print('Data types of columns: ', '\n', df_data.info(verbose=True), '\n')

# Same for "Country" dataframe
print('"Country" columns: ', '\n', df_country.columns, '\n')
print('Duplicates:', '\n', df_country.duplicated(), '\n')
print('Data types of columns: ', '\n', df_country.info(verbose=True), '\n')

# Drop unnecessary columns
df_country = df_country.drop(['Table Name', 'Long Name', '2-alpha code', 'WB-2 code'], axis=1)

# Final shape of each dataframe
print('Data df final shape: ', df_data.shape)
print('Country df final shape: ', df_country.shape)

# Now we have the prepared dataframe for all countries
# However, this ease of doing business country comparison is between Hong Kong and China.
# Only data for Hong Kong and China is required in this context
#data_HKG = df_data['Country Name'] == 'Hong Kong, China'
#df_data_HKG = pd.DataFrame(df_data[data_HKG])
#country_HKG = df_country['Short Name'] == 'Hong Kong SAR, China'
#df_country_HKG = pd.DataFrame(df_country[country_HKG])

#data_CHN = df_data['Country Name'] == 'China'
#df_data_CHN = pd.DataFrame(df_data[data_CHN])
#country_CHN = df_country['Short Name'] == 'China'
#df_country_CHN = pd.DataFrame(df_country[country_CHN])

# Displaying dataframe information
#print('\n Hong Kong score data dataframe info', '\n', df_data_HKG.info(verbose=True))
#print('\n Hong Kong country information dataframe info', '\n', df_country_HKG.info(verbose=True))

#print('\n China score data dataframe info', '\n', df_data_CHN.info(verbose=True))
#print('\n China country information dataframe info', '\n', df_country_CHN.info(verbose=True))
# Null values will be ignored as setting them to 0 isn't representative of the score

# Display Hong Kong and China country information
# Not required for this project, but may be useful in a formal comparison
#print('\n Hong Kong country information:', '\n', df_country_HKG, '\n')
#print('China country information:', '\n', df_country_CHN)

# Removing the redundant information, such as country name and country code
#df_data_HKG = df_data_HKG.iloc[:, 2:]
#df_data_CHN = df_data_CHN.iloc[:, 2:]

# Setting the index to the 'Indicator Name' column
#df_data_HKG.set_index('Indicator Name', inplace=True)
#df_data_CHN.set_index('Indicator Name', inplace=True)

#print('\n Hong Kong country information:', '\n', df_data_HKG, '\n')
#print('China country information:', '\n', df_data_CHN)

# Saving the prepared score data as excel spreadsheets
#df_data_HKG.to_excel('hk_data.xlsx')
#df_data_CHN.to_excel('china_data.xlsx')

# Export entire prepared dataframes as csv files to not have to repeat this process every time
df_data.to_csv('prepared_df_data.csv')
df_country.to_csv('prepared_df_country.csv')
