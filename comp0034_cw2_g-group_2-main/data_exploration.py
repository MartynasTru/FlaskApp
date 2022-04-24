import pandas as pd
import matplotlib.pyplot as plt

df_hk = pd.read_excel('hk_data.xlsx', index_col=0)
df_ch = pd.read_excel('china_data.xlsx', index_col=0)

# Display dataframe columns
print('\nHK df columns', df_hk.columns, '\n')
print('China df columns', df_ch.columns)

# Increasing the number of rows and columns displayed
pd.set_option('display.max_rows', df_hk.shape[0] + 1)
pd.set_option('display.expand_frame_repr', False)

# Displaying dataframes for each country
# print('\n Hong Kong scores:', '\n', df_hk, '\n')
# print('China scores:', '\n', df_ch, '\n')

# Displaying a general analysis using pandas
print('\nHong Kong score data analysis: ', '\n', df_hk.describe(), '\n')
print('China score data analysis: ', '\n', df_ch.describe(), '\n')
# From this, we can see that the dataframes need to be transposed to correctly use the describe() function,
# because we want to compare the countries based on their scores in a category, not in a year.
df_hk_t = df_hk.T
df_ch_t = df_ch.T

# Displaying the now transposed dataframes for each country
print('\n Hong Kong scores (t):', '\n', df_hk_t, '\n')
print('China scores (t):', '\n', df_ch_t)

# Display dataframe columns representing the score categories
print('HK df columns', df_hk_t.columns, '\n')
print('China df columns', df_ch_t.columns, '\n')

# Displaying a general analysis of the transposed dataframes
print('Hong Kong score data analysis: ', '\n', df_hk_t.describe())
print('China score data analysis: ', '\n', df_ch_t.describe())
# From this quick and general analysis, we can see that Hong Kong has the higher mean, thus a higher rank, in most
# categories

# We now have the dataframes for Hong Kong and China, which will be used to answer the questions.
print('\nComparison datasets:\n')

# Does Hong Kong or China deal better with construction permits?
# The permit score (DB16-20 method) from 2014 to 2020
hk_constr_permit_score1620 = df_hk_t.iloc[:, 1:2]
ch_constr_permit_score1620 = df_ch_t.iloc[:, 1:2]

print('Hong Kong construction permit score:', '\n', hk_constr_permit_score1620, '\n')
print('China construction permit score:', '\n', ch_constr_permit_score1620, '\n')

df_constr_permit_score1620 = pd.concat([hk_constr_permit_score1620, ch_constr_permit_score1620], axis=1)

# Removing rows 2014 because it is empty for both
df_constr_permit_score1620.drop([df_constr_permit_score1620.index[0]], inplace=True)

# Checking that the values are numerical
print(df_constr_permit_score1620.info(verbose=True))

# Plotting data
# An unstacked bar plot is used because we are comparing yearly scores for two sets of data
df_constr_permit_score1620.plot(kind='bar')
plt.title('Dealing with construction permits (DB16-20 methodology) score')
plt.xlabel('Score (%)')
plt.ylabel('Year')
plt.legend(['Hong Kong', 'China'])
plt.show()
# Saving plot as a png file
plt.savefig('construction_permits_plot.png')

# The time to approve a building permit in days score from 2014 to 2020
hk_constr_permit_time_score = df_hk_t.iloc[:, 15:16]
ch_constr_permit_time_score = df_ch_t.iloc[:, 15:16]

print('Hong Kong time to approve a building permit (in days) score:', '\n', hk_constr_permit_time_score, '\n')
print('China time to approve a building permit (in days) score:', '\n', ch_constr_permit_time_score, '\n')

df_contr_permit_time_score = pd.concat([hk_constr_permit_time_score, ch_constr_permit_time_score], axis=1)

# Checking that the values are numerical
print(df_contr_permit_time_score.info(verbose=True))

# Plotting data
df_contr_permit_time_score.plot(kind='bar')
plt.title('Time to deal with construction permits score')
plt.xlabel('Score (%)')
plt.ylabel('Year')
plt.legend(['Hong Kong', 'China'])
plt.show()
# Saving plot as a file
plt.savefig('construction_permits_time_plot.png')

# From this, we can see that Hong Kong has a significantly higher score than China both for dealing with construction
# permits and the time it takes to approve a permit. It can therefore be said that Hong Kong deals better with
# construction permits.
# That being said, China has been improving on both fronts over the years.


# Is international trade easier in Hong Kong or China?
hk_trade = df_hk_t.iloc[:, 182:183]
ch_trade = df_ch_t.iloc[:, 182:183]

print('Hong Kong trade across borders (DB16-20) score:', '\n', hk_trade, '\n')
print('China trade across borders (DB16-20) score:', '\n', ch_trade, '\n')

df_trade = pd.concat([hk_trade, ch_trade], axis=1)

# Removing rows 2014 because it is empty for both
df_trade.drop([df_trade.index[0]], inplace=True)

# Checking that the values are numerical
print(df_trade.info(verbose=True))

# Plotting data
df_trade.plot(kind='bar')
plt.title('Trading across borders score (DB16-20 methodology)')
plt.xlabel('Score (%)')
plt.ylabel('Year')
plt.legend(['Hong Kong', 'China'])
plt.show()
# Saving plot as a file
plt.savefig('international_trade_plot.png')

# From this plot, we can see that international trade is easier in Hong Kong than it is in China.


# Is starting a business easier in Hong Kong or China?
hk_starting_business = df_hk_t.iloc[:, 160:161]
ch_starting_business = df_ch_t.iloc[:, 160:161]

print('Hong Kong starting a business score:', '\n', hk_starting_business, '\n')
print('China starting a business score:', '\n', ch_starting_business, '\n')

df_starting_business = pd.concat([hk_starting_business, ch_starting_business], axis=1)

# Checking that the values are numerical
print(df_starting_business.info(verbose=True))

# Plotting data
df_starting_business.plot(kind='bar')
plt.title('Starting a business score')
plt.xlabel('Score (%)')
plt.ylabel('Year')
plt.legend(['Hong Kong', 'China'])
plt.show()
# Saving plot as a file
plt.savefig('starting_business_plot.png')

# Thus, Hong Kong is more favourable to starting a business, but not by much. Indeed, recently China has improved and
# there wasn't much separating them in 2020.


# Which of the two has a better ease of doing business (DB17-20) score?
hk_ease_business1720 = df_hk_t.iloc[:, 77:78]
ch_ease_business1720 = df_ch_t.iloc[:, 77:78]

print('Hong Kong ease of doing business score (DB17-20):', '\n', hk_ease_business1720, '\n')
print('China ease of doing business score (DB17-20):', '\n', ch_ease_business1720, '\n')

df_business = pd.concat([hk_ease_business1720, ch_ease_business1720], axis=1)

# Removing rows 2014 and 2015 because they are empty for both
df_business.drop([df_business.index[0], df_business.index[1]], inplace=True)

# Checking that the values are numerical
# Print column info
print(df_business.info(verbose=True))

# Plotting data
df_business.plot(kind='bar')
plt.title('Ease of doing business score (DB17-20 methodology)')
plt.xlabel('Score (%)')
plt.ylabel('Year')
plt.legend(['Hong Kong', 'China'])
plt.show()
# Saving plot as a file
plt.savefig('doing_business_plot.png')

# Once again, despite China improving in 2020, Hong Kong nevertheless has a higher ease of doing business score.
# As such, it can be said that although being under China's control will likely not help Hong Kong from an economic
# standpoint, China is improving and will likely not hinder Hong Kong much in the years to come.
