# sqlalchemy-challenge

Couple different parts to this one:

First, we are analyzing the weather for our dream vacation destination -- Honolulu, Hawaii!! We have a sqllite database with temperature and precipitation information from various observation stations. We're using SQLalchemy to link to our database and query for our information.

## What do the last 12 months of precipation data look like?

*One caveat here: this graph includes data from all stations, but plots along a  timeline. This makes the graph misleading, since each date will have multiple bars with it (i.e. '2016-08-23' will have potentially 9 different bars on our graph). Future fix for this would be looking at each station separately.*

![Precipitation chart](https://github.com/LongPatrol/sqlalchemy-challenge/blob/main/Pictures/Precip_bar_chart.png)


## What are some summary statistics on our precipitation data?

![Precipitation stats](https://github.com/LongPatrol/sqlalchemy-challenge/blob/main/Pictures/Precip_summary_stats.png)



# Sources:
**How to order by descending in SQLalchemy:**

https://stackoverflow.com/questions/4186062/sqlalchemy-order-by-descending

**Filtering in SQLalchemy:**

https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_filter_operators.htm

**Date offset in pandas:**

https://stackoverflow.com/questions/31169774/subtract-a-year-from-a-datetime-column-in-pandas

**Converting to datetime:**

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html

**Date of a datetime index:**

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DatetimeIndex.date.html

**Dataframe.plot:**

https://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.plot.html

**Legend:**

https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.legend.html

**Showing the whole legend label:**

https://stackoverflow.com/questions/10557614/matplotlib-figlegend-only-printing-first-letter

**Session querying:**

https://docs.sqlalchemy.org/en/13/orm/query.html

**Order by descending:**

https://stackoverflow.com/questions/4186062/sqlalchemy-order-by-descending

**Loops only giving first value:**

https://stackoverflow.com/questions/52118391/stuck-with-loops-in-python-only-returning-first-value

**Isnull:**

https://www.geeksforgeeks.org/python-pandas-isnull-and-notnull/

**Variables in flask:**

https://hackersandslackers.com/flask-routes/

**Date issue for plotting the precip:**

https://stackoverflow.com/questions/62200296/python-dates-in-wrong-order
