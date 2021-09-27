
from dash_package.models import Strain, Flavor, Effect, Country, StrainFlavor, StrainEffects, StrainCountry
# from sqlalchemy import create_engine, func
# from sqlalchemy.orm import sessionmaker, relationship
from collections import Counter
# engine = create_engine('sqlite:///weed.db')
# Session = sessionmaker(bind=engine)
# session = Session()

# CHANGE QUERIES from session.query(Listing).all() to Listing.query.all()/filter_by()

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

def races():
    objs = Strain.query.all()
    races = list(map(lambda o: o.race, objs))
    return list(set(races))

def strain_names_by_race(race):
    objs = Strain.query.filter(Strain.race == race).all()
    names = list(map(lambda o: o.name, objs))
    return names

def count_by_race():
    race_counts = list(map(lambda r: (r, len(strain_names_by_race(r))), races()))
    return {'x': list(map(lambda c: c[0], race_counts)), 'y': list(map(lambda c: c[1], race_counts))}


def flavors():
    objs = Strain.query.all()
    flavors = []
    for o in objs:
        for flavor in o.flavors:
            flavors.append(flavor.name)
    return list(set(flavors))

def strain_names_by_flavor(flavor):
    objs = Flavor.query(Flavor).filter(Flavor.name == flavor).first().strains
    names = list(map(lambda o: o.name, objs))
    return names

def count_by_flavor():
    flavor_counts = list(map(lambda f: (f, len(strain_names_by_flavor(f))), flavors()))
    return {'x': list(map(lambda f: f[0], flavor_counts)), 'y': list(map(lambda f: f[1], flavor_counts))}


def effects():
    objs = Strain.query.all()
    effects = []
    for o in objs:
        for effect in o.effects:
            effects.append(effect.name)
    return list(set(effects))

def strain_names_by_effect(effect):
    objs = Effect.query.filter(Effect.name == effect).first().strains
    names = list(map(lambda o: o.name, objs))
    return names

def count_by_effect():
    effect_counts = list(map(lambda e: (e, len(strain_names_by_effect(e))), effects()))
    return {'x': list(map(lambda f: f[0], effect_counts)), 'y': list(map(lambda f: f[1], effect_counts))}


def countries():
    objs = Strain.query.all()
    countries = []
    for o in objs:
        for country in o.countries:
            countries.append(country.name)
    return list(set(countries))

def strains_by_country(country):
    return Country.query.filter(Country.name == country).first().strains

def race_count_by_country(country):
    strains = strains_by_country(country)
    race_counts = list(Counter(list(map(lambda s: s.race, strains))).items())
    return {'x': list(map(lambda f: f[0], race_counts)), 'y': list(map(lambda f: f[1], race_counts))}


def effect_count_by_country(country):
    strains = strains_by_country(country)
    effects = []
    for strain in strains:
        straineffects = strain.effects
        for effect in straineffects:
            effects.append(effect.name)
    effect_counts = list(dict(Counter(effects)).items())
    return {'x': list(map(lambda f: f[0], effect_counts)), 'y': list(map(lambda f: f[1], effect_counts))}

def country_count_by_effect(effect):
    effect_pick = Effect.query.filter(Effect.name == effect).first()
    strains_with_effect = list(filter(lambda s: effect_pick in s.effects, Strain.query.all()))
    countries = []
    for strain in strains_with_effect:
        countries += strain.countries
    countries_names = list(map(lambda c: c.name, countries))
    country_counts = list(dict(Counter(countries_names)).items())
    return {'x': list(map(lambda f: country_codes[f[0]], country_counts)), 'y': list(map(lambda f: f[1], country_counts))}

def country_count_by_flavor(flavor):
    flavor_pick = Flavor.query.filter(Flavor.name == flavor).first()
    strains_with_flavor = list(filter(lambda s: flavor_pick in s.flavors, Strain.query.all()))
    countries = []
    for strain in strains_with_flavor:
        countries += strain.countries
    countries_names = list(map(lambda c: c.name, countries))
    country_counts = list(dict(Counter(countries_names)).items())
    return {'x': list(map(lambda f: country_codes[f[0]], country_counts)), 'y': list(map(lambda f: f[1], country_counts))}

def flavor_count_by_country(country):
    strains = strains_by_country(country)
    flavors = []
    for strain in strains:
        strainflavors = strain.flavors
        for flavor in strainflavors:
            flavors.append(flavor.name)
    flavor_counts = list(dict(Counter(flavors)).items())
    return {'x': list(map(lambda f: f[0], flavor_counts)), 'y': list(map(lambda f: f[1], flavor_counts))}

def strain_names_by_country(country):
    objs = Country.query.filter(Country.name == country).first().strains
    names = list(map(lambda o: o.name, objs))
    return names

def count_by_country():
    return list(map(lambda c: (c, len(strain_names_by_country(c))), countries()))

def country_race_composition():
    country_list = []
    sativas = []
    indicas = []
    hybrids = []
    for country in countries():
        country_list.append(country)
        race = race_count_by_country(country)['x']
        count = race_count_by_country(country)['y']
        race_dict = dict(zip(race, count))
        if 'sativa' in race_dict.keys():
            sativas.append(race_dict['sativa'])
        if 'indica' in race_dict.keys():
            indicas.append(race_dict['indica'])
        if 'hybrid' in race_dict.keys():
            hybrids.append(race_dict['hybrid'])
    return {'countries': country_list, 'sativas': sativas, 'indicas': indicas, 'hybrids': hybrids}
# top_25_strains = ['Blue Dream', 'Sour Diesel', 'Girl Scout Cookies', 'OG Kush', 'Pineapple Express', 'White Widow', 'Grape Crush', 'White Rhino', 'Green Crack', 'Jack Herer', 'Bubba Kush', 'Gorilla Glue #4', 'Hindu Kush', 'Skywalker OG', 'Trainwreck', 'Purple Kush', 'White OG', 'Skunk #1', 'Purple Goo', 'Afghan Kush', 'Bubble Gum', 'Purple Urkle', 'Grape Ape', 'Purple Haze', 'Lemon Kush']
# def top_25_flavors():
#     flavor_counts = []
#     for bud in top_25_strains:
#         for strain in session.query(Strain).all():
#             if bud == strain.name:
#                 for flavor in strain.flavors:
#                     flavor_counts.append(flavor.name)
#     return {'x': list(dict(Counter(flavor_counts))), 'y': list(Counter(flavor_counts).values())}
#
# def top_25_races():
#     race_counts = []
#     for bud in top_25_strains:
#         for strain in strains:
#             if bud == strain.name:
#                 race_counts.append(Strain.race)
#     return {'x': list(Counter(race_counts)), 'y': list(Counter(race_counts).values())}
# def top_25_effects():
#     effect_counts = []
#     for bud in top_25_strains:
#         for strain in strains:
#             if bud == strain.name:
#                 effect_counts.append(Strain.effect)
#     return {'x': list(Counter(effect_counts)), 'y': list(Counter(effect_counts).values())}
