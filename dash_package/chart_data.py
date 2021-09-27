from dash_package.models import Strain, Flavor, Effect, Country, StrainFlavor, StrainEffects, StrainCountry
from dash_package.queries import races, strain_names_by_race, count_by_race, country_count_by_flavor
from dash_package.queries import flavors, strain_names_by_flavor, count_by_flavor,  race_count_by_country, effect_count_by_country, flavor_count_by_country, strain_names_by_country
from dash_package.queries import effects, strain_names_by_effect, count_by_effect, countries, strains_by_country, count_by_country, country_race_composition, country_count_by_effect


country_race_composition = country_race_composition()

country_codes = {'Afghanistan': 'AFG',
                'Brazil': 'BRA',
                'Cambodia': 'KHM',
                'Canada': 'CAN',
                'Colombia': 'COL',
                'Congo - Brazzaville': 'COG',
                'Hungary': 'HUN',
                'India': 'IND',
                'Iran': 'IRN',
                'Jamaica': 'JAM',
                'Laos': 'LAO',
                'Malawi': 'MWI',
                'Mexico': 'MEX',
                'Morocco': 'MAR',
                'Nepal': 'NPL',
                'New Zealand': 'NZL',
                'Pakistan': 'PAK',
                'Panama': 'PAN',
                'R\u00e9union': 'MUS',
                'South Africa': 'ZAF',
                'Swaziland': 'SWZ',
                'Switzerland': 'CHE',
                'Thailand': 'THA',
                'Turkey': 'TUR',
                'Ukraine': 'UKR',
                'United States': 'USA',
                'Vietnam': 'VNM'
                }
