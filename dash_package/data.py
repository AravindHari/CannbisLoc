import requests
import json
from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///weed.db')

Session = sessionmaker(bind=engine)
session = Session()

url = 'http://strainapi.evanbusse.com/80Bxz5h/strains/search/all'

data = list(dict(requests.get(url).json()).items())

strain_names = list(requests.get(url).json())

def flavors():
    flavors = []
    for strain in data:
        flavors += strain[1]['flavors']
    return(list(set(flavors)))

def instantiate_flavors():
    flavor_instances = []
    for flavor in flavors():
        flav = Flavor(name=flavor, strains=[])
        flavor_instances.append(flav)
    return flavor_instances

flavor_instances = instantiate_flavors()

def pos_effects():
    pos_effects = []
    for strain in data:
        pos_effects += strain[1]['effects']['positive']
    return list(set(pos_effects))

def neg_effects():
    neg_effects = []
    for strain in data:
        neg_effects += strain[1]['effects']['negative']
    return list(set(neg_effects))

def med_effects():
    med_effects = []
    for strain in data:
        med_effects += strain[1]['effects']['medical']
    return list(set(med_effects))

def effects():
    return pos_effects() + neg_effects() + med_effects()

def instantiate_effects():
    effect_instances = []
    for effect in pos_effects():
        eff = Effect(name=effect, type='Positive', strains=[])
        effect_instances.append(eff)
    for effect in neg_effects():
        eff = Effect(name=effect, type='Negative', strains=[])
        effect_instances.append(eff)
    for effect in med_effects():
        eff = Effect(name=effect, type='Medical', strains=[])
        effect_instances.append(eff)
    return effect_instances

effect_instances = instantiate_effects()

json_data=open('location-data.json').read()
lineage_data = json.loads(json_data)
lineages = list(lineage_data.items())

strains_with_lineages = list(filter(lambda s: s[0] in strain_names, lineages))

def countries():
    countries = []
    for strain in strains_with_lineages:
        countries += strain[1]
    return list(set(countries))

def instantiate_countries():
    country_instances = []
    for country in countries():
        ctry = Country(name=country, strains=[])
        country_instances.append(ctry)
    return country_instances

country_instances = instantiate_countries()
dict_with_lineages = dict(filter(lambda s: s[0] in strain_names, lineages))
names_with_lineages = list(dict_with_lineages)

def instantiate_strains():
    strain_instances = []
    for strain in data:
        if strain[0] in names_with_lineages:
            s = Strain(name=strain[0], \
                race=strain[1]['race'], \
                flavors=list(filter(lambda f: f.name in strain[1]['flavors'], \
                    flavor_instances)), \
                effects=list(filter(lambda e: e.name in strain[1]['effects']['positive'] or \
                                                e.name in strain[1]['effects']['negative'] or \
                                                e.name in strain[1]['effects']['medical'], effect_instances)),
                countries=list(filter(lambda c: c.name in dict_with_lineages[strain[0]], country_instances)))
        else:
            s = Strain(name=strain[0], \
                race=strain[1]['race'], \
                flavors=list(filter(lambda f: f.name in strain[1]['flavors'], \
                    flavor_instances)), \
                effects=list(filter(lambda e: e.name in strain[1]['effects']['positive'] or \
                                                e.name in strain[1]['effects']['negative'] or \
                                                e.name in strain[1]['effects']['medical'], effect_instances)),
                countries=[])
        strain_instances.append(s)
    return strain_instances

strain_instances = instantiate_strains()


session.add_all(flavor_instances)
session.add_all(effect_instances)
session.add_all(country_instances)
session.add_all(strain_instances)
session.commit()
