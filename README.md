# sqlalchemy-challenge

Couple different parts to this one:

First, we are analyzing the weather for our dream vacation destination -- Honolulu, Hawaii!! We have a sqllite database with temperature and precipitation information from various observation stations. We're using SQLalchemy to link to our database and query for our information.

## What do the last 12 months of precipation data look like?

*One caveat here: this graph includes data from all stations, but plots along a  timeline. This makes the graph misleading, since each date will have multiple bars with it (i.e. '2016-08-23' will have potentially 9 different bars on our graph). Future fix for this would be looking at each station separately.



