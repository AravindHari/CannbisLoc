# Alchemy Has No Negative Side Effects
In this data visualization project, we explore the characteristics of cannabis strains.

Project partner: [Adam Liscia](https://github.com/AdamLiscia)

#### Our Two APIs
* StrainAPI - strains, flavors, effects
* Otreeba - strains, lineages

### Our Project
We decided to explore the race, flavors, effects of marijuana strains based on their lineage. We pulled this data from two APIs. 1970 strains from StrainAPI and over 9000 strains from Otreeba. There happened to be an overlap of 772 strains that had full data.

Using Dash, Plotly and Flask for the front end and SQLAlchemy for creating the ORM, we put together a dashboard to visualize the data from these 772 strains.

## The App

The Dash app can be run by cloning the repository and doing `python run.py` in the command line, through the local host URL.

## Visualizations (Screenshots of Dash App)

1. Bar graph showing number of strains coming from each country, separated by race (indica, sativa, hybrid). Note: each strain can be traced back to more than one country, based on its lineage.

![header](images/race-country-bar.png)

2. Pie chart showing the distribution of strain races per country, with dropdown country selector.

![header](images/race-per-country.png)

3. Pie chart showing the distribution of strain effects per country, with dropdown country selector.

![header](images/effect-per-country.png)

4. Pie chart showing the distribution of strain flavors per country, with dropdown country selector.

![header](images/flavor-per-country.png)

5. Choropleth map showing the distribution of a strain effect, with dropdown effect selector.

![header](images/effect-map.png)

6. Choropleth map showing the distribution of a strain flavor, with dropdown flavor selector.

![header](images/flavor-map.png)
