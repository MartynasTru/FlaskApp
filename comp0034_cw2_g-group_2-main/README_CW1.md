## 1. [Coursework Github repository url](https://github.com/ucl-comp0035/comp0034-cw1-g-group_2.git)

## 2. Explanation and evaluation of the chosen visualisations

1. Table:
   1. The target audience of the table visualisation in this case would be people who want to compare the evolution of
      the scores of multiple countries over a number of years in detail. Such an audience could include legislators, who
      could be looking into slight fluctuations in trade or construction scores, to observe the success of laws in a
      particular sector.
      This data visualisation type is less visually illustrative of data trends than others, but is useful when the data
      characteristics are known and the samples are limited. It allows the user to pay more attention to the individual
      data points.
   2. This dataset contains the yearly scores of different countries in a multitude of categories. As such, the table
      will give the scores of the selected countries in a single selected category over the desired years. This will
      allow the user to easily identify and compare the precise yearly score of the desired countries.
      Since only one category can be chosen, it will not be indicated in the table but rather in its title.
   3. The resulting table visualisation is coherent with the design. However, in this case as the data is only given on
      a yearly basis, there is not as much need for the more detail-oriented approach that the table provides. If the
      dataset contained data collected at a smaller time interval, the table would be more useful.

2. Single-bar chart (single bar per country):
   1. The target audience of the single-bar chart would be people who want to compare the scores of countries in a
      single category and a single year. This visualisation allows for an easy comparison of the performance of
      the countries as the bar height is proportional to the score, which allows users to identify the best and worst
      performers at a glance. Such an audience could include businesspeople who are looking to analyse the performance
      trends of neighbouring countries to identify a suitable market to expand into.
   2. The design of the single-bar chart will include a bar that is proportional to the country score above the country
      code. The x-axis will thus be the different countries that the user selects, with the y-axis being the score.
   3. Again, the resulting single-bar chart is as designed. It works as intended, clearly indicating the best performing
      country in the desired category and over the desired year. A main weakness of this visualisation type is that the
      specific scores aren't displayed, however this is addressed by the tooltip which appears when hovering over the
      bars.

3. Multiple-bar chart (multiple bars per country):
   1. The target audience for the multiple-bar chart visualisation is similar to that of the single-bar chart.
      However, this visualisation allows for the comparison of the performance of multiple countries over multiple
      years. This is useful for comparing both how a country's score progresses, as well as how the selected countries' 
      scores relate to one-another.
   2. Like the single-bar chart, this visualisation uses bars that are proportional to the country's score above the
      country code. As such, the x-axis is the countries and the y-axis is the score. In this case, seeing as there can
      be multiple selected years, each country will have a number of bars illustrating their scores over each year, with
      the number of bars per country being the number of years the user has selected.
      The bars for each year will differ in colour, with a colour legend on the right side of the visualisation
      indicating which coloured bars represent which year.
   3. The resulting visualisation is as designed. Each country has a number of coloured bars representing their scores
      per year. The contrasting colours of the bars clearly indicates the difference between the years. It contains more
      information than the single-bar chart, which allows for both a comparison of the country's progression over the
      years and a comparison between countries. Again, there is the issue of the precise score not being shown, which is
      addressed by the hovering tooltip. A potential drawback with this visualisation type is that it can get cluttered
      and lose detail the more there are countries and years as the size of each bar depends on the number of total
      bars, which could be inconvenient to the user.

4. Matrix heatmap:
   1. The target audience for the matrix heatmap visualisation are people who would want to compare multiple countries'
      score in a category over multiple years. It uses variances in the colour of each of the matrix's cells to depict
      variations in data. The matrix heatmap allows for  data to be represented, as the colour of the cell also
      represents a variable, which means that the data is still legible even when concentrated into small cells. 
      As such, the matrix heat map enables the user to quickly identify patterns and outliers in the data.
   2. The matrix heatmap uses variances in the colour of each of the matrix's cells to depict variations in data. In
      this case, the colour of the cell will depend on the score of the country over a certain year. A legend indicating
      the score bracket that the colour gradient represents will be present on the right side of the visualisation.
   3. Overall, the matrix heatmap visualisation is faithful to the design. The strengths of this visualisation type are
      especially apparent when selecting a lot of countries and years. Indeed, since the size of each cell decreases the
      more cells there are, patterns shown through the cells colour become more apparent as the resolution of the
      resulting 'image' or combination of pixels increases. However, this advantage may become a fault when used with a
      different dataset that contains more years of data, as the patterns may not retain their detail and would instead
      reveal trends on a greater scale.

5. Pie chart:
   1. The target audience of the pie chart data visualisation type are people who would want to see the proportion of
      the scores of each country in a category. This can be used to compare countries by highlighting the differences in
      score between them through a difference in percentage and coloured area. The target audience could include
      business owners or prospective investors who would want to compare potential investment opportunities based on the
      country's performance.
   2. The design of the pie chart will consist of a circle divided into 'slices', the arc length of which represents the
      score of the country in proportion with the scores of the countries it is being compared to. The slice of each
      country will have its own colour. The category in question is indicated in the pie chart's title.
   3. The resulting pie chart visualisation is similar to the design and functions as expected. However, the amount of
      data, and its intricacy, that can be represented using a pie chart is limited. This could be 
      improved by attributing similar colours to countries in the same regions or continents, which would allow for the 
      comparison between related regions based on their proportional scores in a category to find business trends.
   
## 3. References

1. [Dash plotly adding custom styling for different html div's](https://stackoverflow.com/questions/50844844/python-dash-custom-css)
2. [Dash plotly adding callbacks and examples](https://dash.plotly.com/basic-callbacks)
3. [Dash core components that were used for the coursework](https://dash.plotly.com/dash-core-components)
4. [Great example of professional dashboard](https://towardsdatascience.com/create-a-professional-dasbhoard-with-dash-and-css-bootstrap-e1829e238fc5)
5. [Plotly figure examples](https://plotly.com/python/figure-labels/)
6. [Legend title manipulation](https://stackoverflow.com/questions/64371174/plotly-how-to-change-variable-label-names-for-the-legend-in-a-plotly-express-li)

