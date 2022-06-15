
"""Modelos

Módulo que contiene los modelos en base de datos.
"""
from . import db


class CfgParameters(db.Model):
    __tablename__ = 'cfg_parameters'
    id = db.Column(db.Integer, primary_key=True, index=True)
    profile_name = db.Column(db.String(255), unique=True, nullable=False)
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


    def to_json(self):
        return {
            'id': self.id,
            'profile_name': self.profile_name,
            'material_cost': self.material_cost,
            'material_density': self.material_density,
            'spool_weigth' : self.spool_weigth,
            'electric_cost': self.electric_cost,
            'printer_power': self.printer_power,
            'printer_price': self.printer_price,
            'amortization_years': self.amortization_years,
            'daily_printer_time' : self.daily_printer_time,
            'failure_rate_prcent': self.failure_rate_prcent,
            'workforce_cost': self.workforce_cost,
            'measure_unit': self.measure_unit
        }
