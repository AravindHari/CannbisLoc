from dash_package import db

class Strain(db.Model):
    __tablename__ = 'strains'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    race = db.Column(db.Text)
    flavors = db.relationship('Flavor', secondary='strainflavors', back_populates='strains')
    effects = db.relationship('Effect', secondary='straineffects', back_populates='strains')
    countries = db.relationship('Country', secondary='straincountries', back_populates='strains')

class Flavor(db.Model):
    __tablename__ = 'flavors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    strains = db.relationship('Strain', secondary='strainflavors', back_populates='flavors')

class StrainFlavor(db.Model):
    __tablename__ = 'strainflavors'
    strain_id = db.Column(db.Integer, db.ForeignKey('strains.id'), primary_key=True)
    flavor_id = db.Column(db.Integer, db.ForeignKey('flavors.id'), primary_key=True)

class Effect(db.Model):
    __tablename__ = 'effects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    type = db.Column(db.Text)
    strains = db.relationship('Strain', secondary='straineffects', back_populates='effects')

class StrainEffects(db.Model):
    __tablename__ = 'straineffects'
    strain_id = db.Column(db.Integer, db.ForeignKey('strains.id'), primary_key=True)
    effect_id = db.Column(db.Integer, db.ForeignKey('effects.id'), primary_key=True)

class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    strains = db.relationship('Strain', secondary='straincountries', back_populates='countries')

class StrainCountry(db.Model):
    __tablename__ = 'straincountries'
    strain_id = db.Column(db.Integer, db.ForeignKey('strains.id'), primary_key=True)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), primary_key=True)


# engine = create_engine('sqlite:///weed.db')
# Base.metadata.create_all(engine)
