
"""Modelos

Módulo que contiene los modelos en base de datos.
"""
from . import db


class CfgProfile(db.Model):
    __tablename__ = 'cfg_profile'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)


class CfgParameters(db.Model):
    __tablename__ = 'cfg_parameters'
    id = db.Column(db.Integer, primary_key=True)
    profile  = db.Column(db.Integer, db.ForeignKey('cfg_profile.id'))
    material_cost = db.Column(db.Integer, nullable=False)
    material_density = db.Column(db.Float, nullable=False)
    spool_weigth = db.Column(db.Integer, nullable=False)
    electric_cost = db.Column(db.Float, nullable=False)
    printer_power = db.Column(db.Float, nullable=False)
    printer_price = db.Column(db.Float, nullable=False)
    amortization_years = db.Column(db.Integer, nullable=False)
    daily_printer_time = db.Column(db.Float, nullable=False)
    failure_rate_prcent = db.Column(db.Float, nullable=False)
    workforce_cost = db.Column(db.Float, nullable=False)
    measure_unit = db.Column(db.Boolean, nullable=False)

    relprof = db.relationship('CfgProfile')

    def to_json(self):
        pass




